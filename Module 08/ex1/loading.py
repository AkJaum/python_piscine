import importlib
import sys


REQUIRED_PACKAGES = {
	"pandas": "Data manipulation ready",
	"numpy": "Numerical computation ready",
	"matplotlib": "Visualization ready",
}


def get_package_version(module):
	"""Return a display-friendly package version string."""
	version = getattr(module, "__version__", None)
	if version is None:
		return "unknown"
	return str(version)


def check_dependencies():
	"""Import dependencies lazily and report status without crashing."""
	loaded = {}
	missing_required = []

	print("Checking dependencies:")

	for package_name, message in REQUIRED_PACKAGES.items():
		try:
			module = importlib.import_module(package_name)
			loaded[package_name] = module
			print(f"[OK] {package_name} ({get_package_version(module)}) - {message}")
		except ImportError:
			missing_required.append(package_name)
			print(f"[MISSING] {package_name} - required for this program")
	return loaded, missing_required


def show_install_help(missing_required):
	"""Display installation guidance for both dependency managers."""
	missing_list = ", ".join(missing_required)
	print("\nMissing required dependencies:", missing_list)
	print("Install with pip:")
	print("  pip install -r requirements.txt")
	print("Install with Poetry:")
	print("  poetry install")


def analyze_matrix_data(np_module, pd_module, mpl_module):
	"""Generate simulated Matrix data, analyze it, and save a plot."""
	print("\nAnalyzing Matrix data...")

	point_count = 1000
	print(f"Processing {point_count} data points...")

	rng = np_module.random.default_rng(seed=42)
	cycle = np_module.arange(point_count)
	signal = np_module.sin(cycle / 25.0) + rng.normal(0.0, 0.2, point_count)
	system_load = np_module.clip(0.5 + 0.4 * signal + rng.normal(0.0, 0.08, point_count), 0, 1)
	anomaly_score = np_module.abs(signal - np_module.mean(signal))

	frame = pd_module.DataFrame(
		{
			"cycle": cycle,
			"signal": signal,
			"system_load": system_load,
			"anomaly_score": anomaly_score,
		}
	)

	print("Summary statistics:")
	print(f"- Average signal: {frame['signal'].mean():.4f}")
	print(f"- Maximum signal: {frame['signal'].max():.4f}")
	print(f"- Average system load: {frame['system_load'].mean():.4f}")
	print(f"- Peak anomaly score: {frame['anomaly_score'].max():.4f}")

	print("Generating visualization...")
	figure, axis = mpl_module.pyplot.subplots(figsize=(10, 5))
	axis.plot(frame["cycle"], frame["signal"], linewidth=1.2, label="Signal")
	axis.plot(frame["cycle"], frame["system_load"], linewidth=1.2, label="System load")
	axis.set_title("Matrix Simulation: Signal and Load")
	axis.set_xlabel("Cycle")
	axis.set_ylabel("Value")
	axis.grid(alpha=0.3)
	axis.legend()

	output_path = "matrix_analysis.png"
	figure.tight_layout()
	figure.savefig(output_path, dpi=150)
	mpl_module.pyplot.close(figure)

	print("Analysis complete!")
	print(f"Results saved to: {output_path}")


def main():
	print("LOADING STATUS: Loading programs...")

	modules, missing_required = check_dependencies()
	if missing_required:
		show_install_help(missing_required)
		return 1
	np_module = modules["numpy"]
	pd_module = modules["pandas"]
	mpl_module = modules["matplotlib"]
	analyze_matrix_data(np_module, pd_module, mpl_module)

	return 0


if __name__ == "__main__":
	sys.exit(main())
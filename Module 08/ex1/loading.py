import importlib
import sys


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def get_package_version(module) -> str:
    """Return a display-friendly package version string."""
    version = getattr(module, "__version__", None)
    if version is None:
        return "unknown"
    return str(version)


def check_dependencies() -> tuple[dict[str, object], list[str]]:
    """Import dependencies lazily and report status without crashing."""
    loaded = {}
    missing_required = []

    print("Checking dependencies:")

    for package_name, message in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(package_name)
            loaded[package_name] = module
            print(
                f"[OK] {package_name} ({get_package_version(module)})"
                f" - {message}"
            )
        except ImportError:
            missing_required.append(package_name)
            print(f"[MISSING] {package_name} - required for this program")

    return loaded, missing_required


def show_install_help(missing_required) -> None:
    missing_list = ", ".join(missing_required)
    print("\nMissing required dependencies:", missing_list)
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("Install with Poetry:")
    print("  poetry install")


def analyze_matrix_data() -> None:
    """Generate simulated Matrix data and save a visualization."""
    np_module = importlib.import_module("numpy")
    pd_module = importlib.import_module("pandas")
    plt_module = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")

    point_count = 1000
    print(f"Processing {point_count} data points...")

    rng = np_module.random.default_rng(seed=42)
    matrix_index = np_module.arange(point_count)
    signal = np_module.sin(matrix_index / 25.0) + rng.normal(
        0.0,
        0.2,
        point_count,
    )

    frame = pd_module.DataFrame(
        {
            "cycle": matrix_index,
            "signal": signal,
        }
    )
    frame["moving_average"] = frame["signal"].rolling(
        window=20,
        min_periods=1,
    ).mean()

    print("Generating visualization...")
    figure, axis = plt_module.subplots(figsize=(10, 5))
    axis.plot(frame["cycle"], frame["signal"], linewidth=1.1, label="Signal")
    axis.plot(
        frame["cycle"],
        frame["moving_average"],
        linewidth=1.6,
        label="Moving average",
    )
    axis.set_title("Matrix Data Simulation")
    axis.set_xlabel("Cycle")
    axis.set_ylabel("Value")
    axis.grid(alpha=0.3)
    axis.legend()

    output_path = "matrix_analysis.png"
    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt_module.close(figure)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_path}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    modules, missing_required = check_dependencies()
    if missing_required:
        show_install_help(missing_required)
        exit(1)
    analyze_matrix_data()


if __name__ == "__main__":
    sys.exit(main())

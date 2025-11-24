"""Command-line interface (CLI) for the bsort project.

This CLI provides two main commands:
- `train`: Train a machine learning model for bottle cap color detection.
- `infer`: Run inference on a single image.

Usage:
    bsort train --config settings.yaml
    bsort infer --config settings.yaml --image path/to/image.jpg
"""

from __future__ import annotations
import argparse
import yaml
from .train import train
from .infer import infer

def build_parser() -> argparse.ArgumentParser:
    """Create and configure the CLI argument parser.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="bsort",
        description="Bottle cap sorting CLI tool."
    )

    sub = parser.add_subparsers(dest="command", required=True)

    # Train command
    p_train = sub.add_parser("train", help="Train the ML model.")
    p_train.add_argument("--config", "-c", required=True, help="Path to config YAML file.")

    # Infer command
    p_infer = sub.add_parser("infer", help="Run inference on an image.")
    p_infer.add_argument("--config", "-c", required=True, help="Path to config YAML.")
    p_infer.add_argument("--image", "-i", required=True, help="Path to image file.")

    return parser


def main() -> None:
    """Entry point for the bsort CLI."""
    parser = build_parser()
    args = parser.parse_args()

    # Load configuration YAML
    with open(args.config, "r") as f:
        cfg = yaml.safe_load(f)

    # Route commands
    if args.command == "train":
        train(cfg)
    elif args.command == "infer":
        infer(cfg, args.image)
    else:
        raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()

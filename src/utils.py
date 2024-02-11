import argparse
import json
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        choices=[
            "instructblip-vicuna-13b",
            "llava-1.5-13b-hf",
            "blip2-flan-t5-xxl",
            "fuyu-8b",
            'Qwen-VL-Chat'
        ],
    )

    parser.add_argument(
        "--img_path",
        type=str,
        default="images",
    )

    return parser.parse_args()
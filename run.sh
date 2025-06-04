#!/bin/bash

# Simple wrapper to run inference.
# If two arguments are given, treat them as model name and image path.

set -euo pipefail

if [ "$#" -eq 2 ]; then
  python run.py --model "$1" --img_path "$2"
  exit 0
fi

# When no arguments are supplied, run all predefined experiments.
python run.py --model fuyu-8b --img_path ./images/fuyu-8b/quality_3
python run.py --model fuyu-8b --img_path ./images/fuyu-8b/quality_5
python run.py --model fuyu-8b --img_path ./images/fuyu-8b/quality_7
python run.py --model fuyu-8b --img_path ./images/fuyu-8b/size_3
python run.py --model fuyu-8b --img_path ./images/fuyu-8b/size_5
python run.py --model fuyu-8b --img_path ./images/fuyu-8b/size_7

python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/quality_3
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/quality_5
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/quality_7
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/size_3
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/size_5
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/size_7

python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/quality_3
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/quality_5
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/quality_7
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/size_3
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/size_5
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/size_7

python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/quality_3
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/quality_5
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/quality_7
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/size_3
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/size_5
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/size_7

python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/quality_3
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/quality_5
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/quality_7
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/size_3
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/size_5
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/size_7

python run.py --model fuyu-8b --img_path ./images/fuyu-8b/distract_8
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/distract_8
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/distract_8
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/distract_8
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/distract_8

python run.py --model fuyu-8b --img_path ./images/fuyu-8b/distract_12
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/distract_12
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/distract_12
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/distract_12
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/distract_12

python run.py --model fuyu-8b --img_path ./images/fuyu-8b/position_1
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/position_1
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/position_1
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/position_1
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/position_1
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/position_9

python run.py --model fuyu-8b --img_path ./images/fuyu-8b/position_0
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/position_0
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/position_0
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/position_0
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/position_0

python run.py --model fuyu-8b --img_path ./images/fuyu-8b/hcut_6
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/hcut_3
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/hcut_3
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/hcut_3
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/hcut_3

python run.py --model fuyu-8b --img_path ./images/fuyu-8b/vcut_6
python run.py --model blip2-flan-t5-xxl --img_path ./images/blip2-flan-t5-xxl/vcut_3
python run.py --model instructblip-vicuna-13b --img_path ./images/blip2-flan-t5-xxl/vcut_3
python run.py --model llava-1.5-13b-hf --img_path ./images/llava-1.5-13b-hf/vcut_3
python run.py --model Qwen-VL-Chat --img_path ./images/Qwen-VL-Chat/vcut_3


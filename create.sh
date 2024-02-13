python creation.py --model fuyu-8b --task quality --digits 3
python creation.py --model fuyu-8b --task quality --digits 5
python creation.py --model fuyu-8b --task quality --digits 7
python creation.py --model fuyu-8b --task size --digits 3
python creation.py --model fuyu-8b --task size --digits 5
python creation.py --model fuyu-8b --task size --digits 7

python creation.py --model blip2-flan-t5-xxl --task quality --digits 3
python creation.py --model blip2-flan-t5-xxl --task quality --digits 5
python creation.py --model blip2-flan-t5-xxl --task quality --digits 7
python creation.py --model blip2-flan-t5-xxl --task size --digits 3
python creation.py --model blip2-flan-t5-xxl --task size --digits 5
python creation.py --model blip2-flan-t5-xxl --task size --digits 7

python creation.py --model llava-1.5-13b-hf --task quality --digits 3
python creation.py --model llava-1.5-13b-hf --task quality --digits 5
python creation.py --model llava-1.5-13b-hf --task quality --digits 7
python creation.py --model llava-1.5-13b-hf --task size --digits 3
python creation.py --model llava-1.5-13b-hf --task size --digits 5
python creation.py --model llava-1.5-13b-hf --task size --digits 7

python creation.py --model Qwen-VL-Chat --task quality --digits 3
python creation.py --model Qwen-VL-Chat --task quality --digits 5
python creation.py --model Qwen-VL-Chat --task quality --digits 7
python creation.py --model Qwen-VL-Chat --task size --digits 3
python creation.py --model Qwen-VL-Chat --task size --digits 5
python creation.py --model Qwen-VL-Chat --task size --digits 7

python creation.py --model fuyu-8b --task position --digits 3 --distractor_num 0
python creation.py --model blip2-flan-t5-xxl --task position --digits 3 --distractor_num 0
python creation.py --model llava-1.5-13b-hf --task position --digits 3 --distractor_num 0
python creation.py --model Qwen-VL-Chat --task position --digits 3 --distractor_num 0

python creation.py --model fuyu-8b --task position --digits 3 --distractor_num 1
python creation.py --model blip2-flan-t5-xxl --task position --digits 3 --distractor_num 1
python creation.py --model llava-1.5-13b-hf --task position --digits 3 --distractor_num 1
python creation.py --model Qwen-VL-Chat --task position --digits 3 --distractor_num 9

python creation.py --model fuyu-8b --task hcut --digits 6
python creation.py --model blip2-flan-t5-xxl --task hcut --digits 3
python creation.py --model llava-1.5-13b-hf --task hcut --digits 3
python creation.py --model Qwen-VL-Chat --task hcut --digits 3

python creation.py --model fuyu-8b --task vcut --digits 6
python creation.py --model blip2-flan-t5-xxl --task vcut --digits 3
python creation.py --model llava-1.5-13b-hf --task vcut --digits 3
python creation.py --model Qwen-VL-Chat --task vcut --digits 3

python creation.py --model fuyu-8b --task distract --digits 3 --distractor_num 9
python creation.py --model blip2-flan-t5-xxl --task distract --digits 3 --distractor_num 9
python creation.py --model llava-1.5-13b-hf --task distract --digits 3 --distractor_num 9
python creation.py --model Qwen-VL-Chat --task distract --digits 3 --distractor_num 9
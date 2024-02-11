from transformers import AutoProcessor, LlavaForConditionalGeneration, InstructBlipProcessor, InstructBlipForConditionalGeneration, Blip2Processor, Blip2ForConditionalGeneration, AutoModelForVision2Seq, FuyuProcessor, FuyuForCausalLM, AutoTokenizer, AutoModelForCausalLM

import torch


def load_model(args):

    if 'llava' in args.model:
        full_model_name = f"llava-hf/{args.model}"
        processor = AutoProcessor.from_pretrained(full_model_name)
        model = LlavaForConditionalGeneration.from_pretrained(full_model_name, torch_dtype=torch.float16,)
        q_to_instrut = lambda x: f"<image>\nUSER: {x} Answer the question using a single word or phrase.\nASSISTANT:"
        response_to_answer = lambda x: x.split('ASSISTANT:')[1].split('\n')[0].strip()
    elif 'instructblip' in args.model:
        full_model_name = f"Salesforce/{args.model}"
        processor = InstructBlipProcessor.from_pretrained(full_model_name)
        model = InstructBlipForConditionalGeneration.from_pretrained(full_model_name, torch_dtype=torch.float16)
        q_to_instrut = lambda x: f"Question: {x} Short Answer:"
        response_to_answer = lambda x: x.strip()
    elif 'blip2' in args.model:
        full_model_name = f"Salesforce/{args.model}"
        processor = Blip2Processor.from_pretrained(full_model_name)
        model = Blip2ForConditionalGeneration.from_pretrained(full_model_name, torch_dtype=torch.bfloat16)
        q_to_instrut = lambda x: f"Question: {x} Short Answer:"
        response_to_answer = lambda x: x.strip()
    elif 'fuyu' in args.model:
        full_model_name = f"adept/{args.model}"
        processor = FuyuProcessor.from_pretrained(full_model_name)
        model = FuyuForCausalLM.from_pretrained(full_model_name, torch_dtype=torch.bfloat16)
        q_to_instrut = lambda x: f"Question: {x} \nShort Answer:"
        response_to_answer = lambda x: x.split('\x04')[1].strip()
    elif "Qwen" in args.model:
        full_model_name = f"Qwen/{args.model}"
        processor = AutoTokenizer.from_pretrained(full_model_name, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(full_model_name, trust_remote_code=True, fp16=True).eval()
        q_to_instrut = lambda x: f"Question: {x} Answer:"
        response_to_answer = lambda x: x.split('Answer:')[1].strip()
    else:
        raise ValueError("Unsupported model type")

    model.to(args.device)
    return model, processor, q_to_instrut, response_to_answer
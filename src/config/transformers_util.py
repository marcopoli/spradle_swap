from transformers import *
from typing import List, Dict, Any
from src.config import Config
import torch.nn as nn
from termcolor import colored
from transformers.models.cpm import CpmTokenizer
import torch


context_models = {
    'bert-base-uncased' : {  "model": BertModel,  "tokenizer" : BertTokenizerFast },
    'bert-base-multilingual-uncased' : {  "model": BertModel,  "tokenizer" : BertTokenizerFast },
    'bert-base-cased' : {  "model": BertModel,  "tokenizer" : BertTokenizerFast },
    'bert-large-cased' : {  "model": BertModel,  "tokenizer" : BertTokenizerFast },
    'dccuchile/bert-base-spanish-wwm-cased': {  "model": BertModel,  "tokenizer" : BertTokenizerFast },
    'openai-gpt': {"model": OpenAIGPTModel, "tokenizer": OpenAIGPTTokenizer},
    'gpt2': {"model": GPT2Model, "tokenizer": GPT2Tokenizer},
    'ctrl': {"model": CTRLModel, "tokenizer": CTRLTokenizer},
    'transfo-xl-wt103': {"model": TransfoXLModel, "tokenizer": TransfoXLTokenizer},
    'xlnet-base-cased': {"model": XLNetModel, "tokenizer": XLNetTokenizer},
    'xlm-mlm-enfr-1024': {"model": XLMModel, "tokenizer": XLMTokenizer},
    'distilbert-base-cased': {"model": DistilBertModel, "tokenizer": DistilBertTokenizer},
    'roberta-base': {"model": RobertaModel, "tokenizer": RobertaTokenizerFast},
    'roberta-large': {"model": RobertaModel, "tokenizer": RobertaTokenizerFast},
    'xlm-roberta-base': {"model": XLMRobertaModel, "tokenizer": XLMRobertaTokenizerFast},
    'skimai/electra-small-spanish' : {"model": ElectraModel, "tokenizer": ElectraTokenizerFast},
    'google/electra-base-discriminator' : {"model": ElectraModel, "tokenizer": ElectraTokenizerFast},
    'kamalkraj/bioelectra-base-discriminator-pubmed': {"model": ElectraModel, "tokenizer": ElectraTokenizerFast},
    'emilyalsentzer/Bio_ClinicalBERT': {  "model": BertModel,  "tokenizer" : BertTokenizerFast },
    'alvaroalon2/biobert_diseases_ner': {  "model": BertModel,  "tokenizer" : BertTokenizerFast }
}

def get_huggingface_optimizer_and_scheduler(config: Config, model: nn.Module,
                                            num_training_steps: int,
                                            weight_decay: float = 0.0,
                                            eps: float = 1e-8,
                                            warmup_step: int = 0):
    """
    Copying the optimizer code from HuggingFace.
    """
    print(colored(f"Using AdamW optimizeer by HuggingFace with {config.learning_rate} learning rate, "
                  f"eps: {eps}, weight decay: {weight_decay}, warmup_step: {warmup_step}, ", 'yellow'))
    no_decay = ["bias", "LayerNorm.weight"]
    optimizer_grouped_parameters = [
        {
            "params": [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
            "weight_decay": weight_decay,
        },
        {
            "params": [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)],
            "weight_decay": 0.0,
        },
    ]
    optimizer = AdamW(optimizer_grouped_parameters, lr=config.learning_rate, eps=eps)
    scheduler = get_linear_schedule_with_warmup(
        optimizer, num_warmup_steps=warmup_step, num_training_steps=num_training_steps
    )
    return optimizer, scheduler


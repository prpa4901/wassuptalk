# Model Constants

# GPT-2
GPT2_MODEL_NAME = "gpt2"
GPT2_VOCAB_SIZE = 50257
GPT2_MAX_POSITION_EMBEDDINGS = 1024
GPT2_HIDDEN_SIZE = 768
GPT2_NUM_LAYERS = 12
GPT2_NUM_HEADS = 12

# BERT
BERT_MODEL_NAME = "google-bert/bert-base-uncased"
BERT_VOCAB_SIZE = 30522
BERT_HIDDEN_SIZE = 768
BERT_NUM_LAYERS = 12
BERT_NUM_ATTENTION_HEADS = 12
BERT_INTERMEDIATE_SIZE = 3072

# Falcon (Medium size)
FALCON_MODEL_NAME = "tiiuae/falcon-7b"

# Phi-2
PHI2_MODEL_NAME = "mlx-community/phi-2"

# Mistral (Medium size)
MISTRAL_MODEL_NAME = "mistralai/Mistral-7B-v0.1"

# Common constants
MAX_LENGTH = 512
BATCH_SIZE = 32
LEARNING_RATE = 5e-5
NUM_TRAIN_EPOCHS = 3
WARMUP_STEPS = 500
WEIGHT_DECAY = 0.01

# Special tokens
PAD_TOKEN = "[PAD]"
UNK_TOKEN = "[UNK]"
CLS_TOKEN = "[CLS]"
SEP_TOKEN = "[SEP]"
MASK_TOKEN = "[MASK]"

# Device settings
# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

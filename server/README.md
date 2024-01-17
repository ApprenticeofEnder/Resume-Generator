# ResGen Server

## Installation

### 1. Create Environment
```bash
cp -r sample_env env
```

Now, configure:
```bash
# env/dev.env
DATA_DIR=data
```

```bash
# env/prod.env
DATA_DIR=/app/data
```

### 2. Install
```bash
poetry install
```

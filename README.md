# DeepFilterNet testing

### Install requirements
```sh
pip install -r requirements.txt
```

### Run DFN on the sample noisy audio files:
```sh
python main.py
```
The processed output files will be written to an `output` folder.

### Run DFN on Modal serverless:
```sh
modal run modal_app.py --name noisy_snr0.wav    # or any wav file in samples
```
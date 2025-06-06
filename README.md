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

### Comparison with Krisp
All the files in `samples` ending with `_before.wav` are taken directly from Krisp's [AI Noise Cancellation demo](https://krisp.ai/krisp-demo-all-products/).

The respective files de-noised by Krisp are present in the `krisp` directory, which may be compared against the ones in `output`.
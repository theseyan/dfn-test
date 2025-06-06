import modal
import time
import os

app = modal.App(name="dfn-test")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "torch", "torchaudio",
        "deepfilternet",
        "soundfile",
    )
    .apt_install("git")
    .add_local_dir("samples", remote_path="/root/samples")
)

@app.function(image=image)
def enhance(input_path, output_path):
    from df.enhance import enhance, init_df, load_audio, save_audio

    model, df_state, _ = init_df()
    wav_file = os.path.basename(input_path)
    print(f"Processing '{wav_file}'...")
    start_time = time.time()
    audio, _ = load_audio(input_path, sr=df_state.sr())
    num_samples = audio.shape[-1] if hasattr(audio, "shape") else len(audio)
    duration_sec = num_samples / df_state.sr()
    enhanced = enhance(model, df_state, audio)
    save_audio(output_path, enhanced, df_state.sr())
    elapsed_ms = (time.time() - start_time) * 1000
    ratio = (elapsed_ms / 1000) / duration_sec
    print(f"Processed '{wav_file}': duration={duration_sec:.2f}s, processing_time={elapsed_ms:.0f}ms, ratio={ratio:.2f}")

@app.local_entrypoint()
def main(name):
    result = enhance.remote("/root/samples/" + name, "/root/samples/" + name + ".out.wav")
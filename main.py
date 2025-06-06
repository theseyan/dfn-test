import os
import time
from df.enhance import enhance, init_df, load_audio, save_audio

SAMPLES_DIR = "samples"
OUTPUT_DIR = "output"

def ensure_dir_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def process_wav_files(samples_dir, output_dir):
    ensure_dir_exists(output_dir)
    model, df_state, _ = init_df()
    wav_files = [f for f in os.listdir(samples_dir) if f.lower().endswith(".wav")]
    if not wav_files:
        print(f"No WAV files found in {samples_dir}.")
        return

    for wav_file in wav_files:
        input_path = os.path.join(samples_dir, wav_file)
        output_path = os.path.join(output_dir, wav_file)

        print(f"Processing '{wav_file}'...")
        start_time = time.time()

        audio, _ = load_audio(input_path, sr=df_state.sr())
        num_samples = audio.shape[-1] if hasattr(audio, "shape") else len(audio)
        duration_sec = num_samples / df_state.sr()
        enhanced = enhance(model, df_state, audio)
        save_audio(output_path, enhanced, df_state.sr())

        elapsed = (time.time() - start_time) * 1000
        ratio = (elapsed / 1000) / duration_sec
        print(f"Processed '{wav_file}': duration={duration_sec:.2f}s, processing_time={elapsed:.0f}ms, ratio={ratio:.2f}")

if __name__ == "__main__":
    process_wav_files(SAMPLES_DIR, OUTPUT_DIR)
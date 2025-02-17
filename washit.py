import subprocess
import time
import sys
from pathlib import Path
import json

def get_duration(input_path):
    """Get duration of media file in seconds using ffprobe."""
    cmd = [
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',
        '-show_format',
        str(input_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)
    return float(data['format']['duration'])

def process_audio(input_file, output_file):
    """Process audio through NVIDIA Broadcast."""
    # Get duration of input file
    duration = get_duration(input_file)
    print(f"Input file duration: {duration:.2f} seconds")
    
    # Start recording process first with exact duration
    record_process = subprocess.Popen([
        'ffmpeg',
        '-f', 'dshow',
        '-i', 'audio=Microphone (NVIDIA Broadcast)',
        '-t', str(duration + 1),  # Add 1 second buffer
        '-c:a', 'aac',
        '-y',  # Overwrite output file if it exists
        output_file
    ])
    
    # Give recording process a moment to start
    time.sleep(0.5)
    
    # Start playback process with ffplay
    play_process = subprocess.Popen([
        'ffplay',
        '-nodisp',
        '-autoexit',  # Exit when playback finishes
        str(input_file)
    ])
    
    # Wait for playback to finish
    play_process.wait()
    
    # Wait for recording to finish
    record_process.wait()
    
    print(f"Processing complete. Output saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.[wav/mp4/mkv] output.m4a")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = sys.argv[2]
    
    if not input_file.exists():
        print(f"Error: Input file {input_file} does not exist")
        sys.exit(1)
    
    # Allow common audio and video formats
    allowed_extensions = {'.wav', '.mp4', '.mkv', '.avi', '.mov'}
    if not input_file.suffix.lower() in allowed_extensions:
        print("Error: Input file must be one of: "
              f"{', '.join(allowed_extensions)}")
        sys.exit(1)
    
    # Suggest .m4a extension for output if not already
    if not output_file.lower().endswith('.m4a'):
        print("Warning: Recommended output extension is .m4a")
    
    print(f"Processing {input_file} through NVIDIA Broadcast...")
    process_audio(str(input_file), output_file)
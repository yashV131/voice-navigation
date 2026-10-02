# Tier 1 — conversation baseline

## What this is

- User speaks → speech-to-text → LLM replies → text-to-speech speaks it back.
- English only for now.
- The LLM is just plumbing here. Don't spend time on prompting it — any model, even a stub
  echo, is fine. What matters is the voice loop around it.

## Two paths, not one

- **Local (desktop/Tauri only)** — runs on-device, no per-call cost. Try `whisper.cpp` /
  `faster-whisper` for STT, something like Piper or Kokoro-82M for TTS.
- **Online (everywhere — web, mobile, and the desktop fallback)** — a cloud STT/TTS API. Web and
  mobile can't reliably run heavy local models, so this is the default path there.

## What to measure

- STT accuracy (word error rate) and latency.
- TTS naturalness and latency.
- End-to-end turn latency — measure where the time actually goes (LLM inference is usually the
  biggest chunk, not the speech legs — check whether that's true here too).

## Design note

Build one interface both paths implement — something like:

```
transcribe(audio) -> text
synthesize(text) -> audio
```

Then "local" and "online" are just two implementations of the same interface, swapped per
platform. Don't let the two paths fork into unrelated code.

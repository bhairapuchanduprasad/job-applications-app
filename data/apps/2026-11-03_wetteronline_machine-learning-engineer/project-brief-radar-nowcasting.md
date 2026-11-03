# Project brief: Radar Nowcasting
Repo slug: radar-nowcasting. Status: planned. For: WetterOnline ML Engineer (2026-11-03).

## Goal
Predict the next radar frames from a sequence of public weather radar images with a neural network, and compare against a persistence baseline.

## Why for this JD
Proves PyTorch, NumPy, OpenCV, computer vision, neural networks on radar data, Jupyter-based experimentation, large-data processing.

## Scope (1-2 days)
- Data: public radar composites (e.g. DWD RADOLAN open data), a few weeks of frames; convert to NumPy arrays, OpenCV resize/normalise/mask.
- Baseline: persistence (last frame) and optical-flow extrapolation (OpenCV).
- Model: small U-Net or ConvLSTM in PyTorch, predict +5/+10/+30 min frames.
- Evaluation: per-lead-time MSE and CSI at rain thresholds, side-by-side frame GIFs.
- Optional stretch: vectorise a hot loop with NumPy / note on C++/OpenMP port.

## Tech stack
Python, PyTorch, NumPy, OpenCV, Jupyter, Git.

## Architecture sketch
download -> arrays (.npy) -> windowed dataset -> model -> metrics + GIF notebook.

## Milestones
1. Data loader + preprocessing. 2. Baselines. 3. Model training. 4. Evaluation + GIFs. 5. README.

## README outline
Problem, data source/licence, method, results table (real numbers only after running), limitations.

## Demo idea
GIF: input frames, ground truth, prediction, baseline.

## CV bullet it must live up to
- Predicts upcoming weather radar frames from public radar image sequences: OpenCV preprocessing, a U-Net/ConvLSTM in PyTorch and a persistence baseline, evaluated frame by frame.

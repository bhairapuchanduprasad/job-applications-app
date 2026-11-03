# Brief: Point Cloud Processing Pipeline (Segmantix Founding Engineer)
Goal: show the 3D data-pipeline gap is closable; proves "data pipelines for 3D point cloud data", LIDAR/point clouds, geometry.
Scope (1–2 days): public scans (ModelNet40 / S3DIS or Open3D sample data). Python package: load PLY/PCD, voxel downsample, statistical outlier removal, normal estimation, RANSAC plane segmentation, simple PointNet-style or feature + scikit-learn baseline classifier with per-class precision/recall. FastAPI endpoint (upload scan, return cleaned cloud stats and segments). Docker, pytest, GitHub Actions.
Stack: Python, Open3D, NumPy, scikit-learn/PyTorch, FastAPI, Docker.
Architecture: loaders → processing stages (pure functions, config) → eval script → API.
Milestones: 1 loaders + preprocessing, 2 segmentation + visualisation screenshots, 3 baseline classifier + per-class eval, 4 API + Docker + CI.
README outline: problem, data, pipeline diagram, results table, how to run.
Demo: before/after render of a cleaned scan with detected planes.
CV bullet it must live up to: "Data pipeline for public 3D point cloud scans (e.g. ModelNet, S3DIS): loading, voxel downsampling, outlier removal, normal estimation and RANSAC plane segmentation, with a FastAPI endpoint and a small baseline classifier evaluated per class."

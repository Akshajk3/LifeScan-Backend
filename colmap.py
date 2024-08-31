import pycolmap
import pathlib

# Define paths
output_path = pathlib.Path("point_cloud")
image_dir = pathlib.Path("images")

# Create necessary directories
output_path.mkdir(parents=True, exist_ok=True)
image_dir.mkdir(parents=True, exist_ok=True)
database_path = output_path / "database.db"

# Extract features and match them
pycolmap.extract_features(database_path, image_dir)
pycolmap.match_exhaustive(database_path)

# Perform incremental mapping to generate the sparse point cloud
maps = pycolmap.incremental_mapping(database_path, image_dir, output_path)

# Save the sparse point cloud
maps[0].write(output_path / "sparse.ply")
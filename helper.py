import os
import shutil
import h5py

from pathlib import Path

if __name__ == "__main__":
    grasp_data_paths = list(Path("./grasp_data/mbbchl").glob("*"))
    mesh_paths = list(Path("./objs").glob("*/train/*_visual.obj"))

    for grasp_data_path in grasp_data_paths:
        with h5py.File(grasp_data_path, 'r') as store:
            fname = store.attrs['fname']

        temp = [p for p in mesh_paths if fname in Path(p).stem]
        mesh_path = temp[0]
        assert len(temp) == 1

        obj_type = str(mesh_path).split("/")[1]

        new_dir = os.path.join(
            os.getcwd(), 'grasps', obj_type, 'train'
        )
        os.makedirs(new_dir, exist_ok=True)

        shutil.copy2(
            src=os.path.join(os.getcwd(), grasp_data_path),
            dst=new_dir
        )

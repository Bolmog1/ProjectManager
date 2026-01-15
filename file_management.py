from PySide6.QtCore import QStandardPaths, QDir
import os
import shutil


def ensure_file_exist(filename: str) -> str:
    # Dossier AppLocalDataLocation
    app_data_dir = QStandardPaths.writableLocation(
        QStandardPaths.StandardLocation.AppLocalDataLocation
    )

    # Crée le dossier s'il n'existe pas
    QDir().mkpath(app_data_dir)

    # Chemin final du fichier
    target_path = os.path.join(app_data_dir, filename)

    # Si le fichier n'existe pas → copie depuis le projet
    if not os.path.isfile(target_path):
        project_root = os.path.dirname(os.path.abspath(__file__))
        source_path = os.path.join(project_root, "asset", "generic", filename)

        if not os.path.isfile(source_path):
            raise FileNotFoundError(f"Fichier source introuvable : {source_path}")

        shutil.copyfile(source_path, target_path)

    return os.path.abspath(target_path)

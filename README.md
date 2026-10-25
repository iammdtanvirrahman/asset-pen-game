# Atomic Pen Fighter — Asset Library

This repository contains the 3D assets and a lightweight browser preview for the Pen Fighter tabletop.

## Project structure

```text
asset-pen-game/
├── index.html                         # Three.js asset preview
├── assets/
│   ├── table/
│   │   ├── models/
│   │   │   └── gallinera_table_4k.glb # Main tabletop GLB (upload here)
│   │   ├── textures/                  # External maps, only if not embedded in GLB
│   │   ├── previews/                  # Screenshots / renders
│   │   └── README.md                  # Asset metadata and licensing
│   ├── pens/
│   │   ├── models/
│   │   ├── textures/
│   │   └── previews/
│   ├── environment/
│   └── audio/
├── scripts/
│   └── export_glb.py                  # Optional Blender export helper
└── .github/workflows/
    ├── pages.yml                      # GitHub Pages deployment
    └── convert-glb.yml                # Optional Blender-to-GLB workflow
```

## Table model

Upload the finished model to **`assets/table/models/gallinera_table_4k.glb`**. The preview loads that exact path. If the model uses external textures, keep them in `assets/table/textures/` and make sure their relative paths work from the GLB. A self-contained GLB with embedded textures is preferred.

## Asset standards

- Use GLB/glTF for runtime 3D models.
- Apply transforms and keep polygon counts mobile-friendly.
- Use meters and document dimensions, origin, source, and license.
- Prefer optimized JPEG/WebP color maps; use normal/roughness maps only where they add visible value.
- Test load time and FPS on mobile devices.

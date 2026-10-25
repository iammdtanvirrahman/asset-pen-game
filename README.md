# Pen Fighter — Asset Library

A dedicated asset repository for the **Atomic Pen Fighter** game.

## Asset standards

- **3D models:** GLB/glTF; apply transforms and keep mesh complexity mobile-friendly.
- **Textures:** Prefer WebP/JPEG for color maps and PNG/WebP when alpha is needed.
- **PBR maps:** Base color, normal, and roughness only where they visibly improve the asset.
- **Scale:** Use meters and document each asset's dimensions and origin.
- **Performance:** Target balanced realistic graphics; avoid unnecessary 4K textures and duplicate source exports.
- **Licensing:** Record the source and license for every externally sourced asset.

## Directory layout

```text
assets/
  table/
    models/
    textures/
    previews/
    README.md
  pens/
    models/
    textures/
    previews/
  environment/
  audio/
```

## First milestone: table asset

1. Create or source a realistic school desk/table model.
2. Export the game-ready model as `assets/table/models/school-desk.glb`.
3. Add optimized wood textures under `assets/table/textures/`.
4. Add a preview image and document dimensions, scale, texture maps, source, and license.
5. Test it in the game before adding more assets.

**Note:** Binary models and texture files still need to be uploaded separately; this repository currently starts with documentation only.

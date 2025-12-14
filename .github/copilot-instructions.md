## Purpose

This file gives concise, actionable directions for AI coding agents working on the Elf-Destiny-MAA-Expanded Crusader Kings III mod. Focus on discoverable patterns, file locations, and concrete examples so an agent can make safe edits and additions.

## Quick repo map (what matters)
- `common/culture/innovations/elf_maa_innovations.txt` — culture-specific innovation entries (see pattern under `innovation_*_maa`).
- `common/men_at_arms_types/` — men-at-arms templates; files use numeric prefixes (e.g. `00_...`, `01_...`) for ordering.
- `localization/english/` — YAML localization files; filenames end with `_l_english.yml` (examples: `elf_culture_maa_l_english.yml`, `royal_elf_bloodlines_maa_l_english.yml`).
- `gfx/interface/icons/` — icon assets used by cultural innovations and men-at-arms.
- `gui/elf_maa_texticons.gui` — GUI text/icon mappings for this mod.
- `events/` and `scripted_effects/` — gameplay logic and triggers; changes here often require matching localization keys.

## Project-specific conventions and examples
- Innovations: follow the structure used in `elf_maa_innovations.txt`:
  - `group = culture_group_regional` and `culture_era = culture_era_tribal` are commonly used for region-specific elven innovations.
  - Condition to make the innovation available uses `potential = { has_cultural_parameter = unlock_maa_<region>_innovation }`.
  - Use `unlock_maa = <maa_key>` to unlock MAAs and `flag = global_maa` for cross-region availability.
  - Example snippet (copy pattern and only change keys/values):
    - `innovation_romaviri_maa` uses `has_cultural_parameter = unlock_maa_romaviri_innovation` and three `unlock_maa` lines.

- Men-at-arms: files grouped and prefixed for order. Preserve file header format and naming (do not re-order by filename without checking the `.info` file `common/men_at_arms_types/_men_at_arms_types.info`).

- Localization: every new game string must have an entry in `localization/english/*.yml` under the `l_english:` root and match the exact key used in events, innovations, GUI, or modifiers. Use existing files as templates — do not invent YAML structure.

## Safe-edit checklist for common edits
1. When adding or editing an innovation in `common/culture/innovations/*`:
   - Copy an existing `innovation_*_maa` block and update only keys (name, icon, `potential`, `unlock_maa` lines).
   - Add matching localization keys in `localization/english/<relevant>_l_english.yml`.
   - If a new icon is referenced, place the DDS file in `gfx/interface/icons/` and reference the path exactly.
2. When adding MAA types:
   - Add the definitions into the appropriate `common/men_at_arms_types/*.txt` file following the numeric ordering.
   - Verify `_men_at_arms_types.info` to ensure the file is loaded in the correct order.
3. When changing script/effects/events:
   - Match any `trigger`/`effect` keys to localization and GUI entries.
   - Keep triggers simple and reuse existing helper triggers in `scripted_effects/` where available.

## Files to reference for examples
- Innovation pattern: `common/culture/innovations/elf_maa_innovations.txt`
- MAA groups & ordering: `common/men_at_arms_types/_men_at_arms_types.info` and `common/men_at_arms_types/00_maa_types.txt`
- Localization templates: `localization/english/elf_culture_maa_l_english.yml`
- GUI mapping for texticons: `gui/elf_maa_texticons.gui`
- Scripted effects/triggers: `common/scripted_effects/elven_professionalism_tradition_effects.txt`

## Integration points and external constraints
- The mod targets Crusader Kings III and follows Paradox text-data formats (no compiled build). Changes are loaded by the game; use the in-game debug log (`game/debug.log` when launching with `-debug` flag) to inspect parsing errors.
- Filenames and `*.yml` structure must match Paradox expectations (UTF-8, `l_english:` root). Missing localization entries will show up in-game as the key string.

## What to avoid
- Don't change global prefixes or remove numeric prefixes in the men-at-arms files without checking `_men_at_arms_types.info`.
- Don't create localization keys in other languages before English; add English entries first.

## Quick examples for AI changes
- Add an innovation: copy one `innovation_*_maa` block, change `innovation_<name>_maa` and the `has_cultural_parameter` key, add three `unlock_maa` lines, and add localization entries in `localization/english/`.
- Add localization key:
  - Under `localization/english/new_file_l_english.yml` add:
    ```yml
    l_english:
      my_new_innovation_title: "My innovation title"
      my_new_innovation_desc: "Short description."
    ```

## When you're unsure
- Look for an existing pattern in the exact subfolder (innovations, men_at_arms_types, localization). Prefer copying a minimal working example and editing keys.
- If an edit touches multiple areas (script + localization + gfx), change only one area at a time and validate parsing in-game or via the game log.

---
If anything here is unclear or you'd like me to expand on a specific area (example edits, automated validation scripts, or a loader checklist), tell me which part and I will iterate.

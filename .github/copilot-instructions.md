# Copilot Instructions for Elf Destiny MAA Expanded

## Project Overview
This is a Crusader Kings III mod that expands the "Elf Destiny" submod, focusing on Men-at-Arms (MAA) units, events, and lore. The mod is structured to follow Paradox modding conventions, with custom content for cultures, titles, events, graphics, and localization.

## Directory Structure & Key Components
- `common/`: Core game logic, including casus belli, character interactions, culture, decisions, legacies, men_at_arms_types, modifiers, traits, and scripted effects/triggers.
- `events/`: Event scripts for gameplay, including highguardian, court, diarchy, scheme, war, and overrides for vanilla events.
- `localization/english/`: All English localization files, organized by feature (culture, decisions, events, legacies, modifiers, titles, etc.).
- `gfx/`: Custom graphics for interface, icons, court scenes, and illustrations. DDS format is used for images.
- `gui/`: GUI definitions, e.g., `elf_maa_texticons.gui` for custom icons.
- `history/`: Historical data for cultures and titles.

## Modding Patterns & Conventions
- **Overrides:** Files prefixed with `OVERRIDE_` in `events/` replace or extend vanilla CK3 events. Always check for these before duplicating event logic.
- **Localization:** All new features require corresponding entries in `localization/english/`. Use the `_l_english.yml` suffix and follow Paradox YAML formatting.
- **Men-at-Arms:** New MAA types are defined in `common/men_at_arms_types/` and have matching icons in `gfx/interface/icons/regimenttypes/`.
- **Scripted Effects/Triggers:** Reusable logic is placed in `common/scripted_effects/` and `common/scripted_triggers/`.
- **GUI Icons:** Custom icons for units and features are defined in `.gui` files and referenced in `gfx/interface/icons/`.

## Developer Workflows
- **Testing:** There are no automated tests; testing is manual via CK3 game launch. Always validate changes in-game.
- **Builds:** No build system; simply copy the mod folder to the CK3 `mod` directory and update `descriptor.mod` as needed.
- **Debugging:** Use CK3 debug mode and log files in the game's `AppData/` for troubleshooting.
- **Versioning:** Keep `descriptor.mod` up to date with mod metadata and dependencies.

## Integration Points
- **Steam Workshop:** Main distribution is via Steam (see README for link).
- **Vanilla Game Integration:** Overrides and additions are designed to work alongside vanilla CK3 content. Avoid direct modification of base game files.

## Examples & References
- For new MAA units: Add definitions in `common/men_at_arms_types/`, icons in `gfx/interface/icons/regimenttypes/`, and localization in `localization/english/`.
- For new events: Place scripts in `events/`, add localization, and update relevant triggers/effects.
- For custom GUI: Edit `.gui` files and add supporting graphics in `gfx/`.

## Additional Notes
- Follow Paradox modding best practices for file naming, YAML formatting, and event scripting.
- Avoid generic advice; document only patterns used in this mod.
- Reference the Steam Workshop page for user-facing documentation.

---

If any section is unclear or missing important project-specific details, please provide feedback to improve these instructions.
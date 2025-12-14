# Highguardian Keys Standardization Changelog

Branch: `standardize/highguardian-keys`
Commit message: "Standardize localization keys and event references to 'highguardian' spelling (localization, decisions, effects, interactions, scheme)"

## Summary
This change standardizes dotted localization keys and event references to use the canonical spelling `highguardian` across events, localization, decisions, interactions, and effect localization. Internal IDs such as the trait id `highguard` and men_at_arms id `highguard` were intentionally left unchanged (non-invasive).

## Files edited (representative)
- `localization/english/ep3/highguardian_localization_l_english.yml`
  - Added/standardized many `highguardian.*` keys: `found_highguardian_*`, `send_to_highguardian_*`, `highguardian.*` event strings, single-combat strings, modifiers, and tooltips.
  - Removed duplicate `highguard.*` event blocks where they duplicated the canonical `highguardian.*` entries.

- `common/character_interactions/elf_maa_character_interactions.txt`
  - `desc`, `text`, toast title and tooltip references changed to `send_to_highguardian_*`
  - `save_scope_as = highguardian_candidate`

- `common/effect_localization/elf_maa_effect_localization.txt`
  - Created `send_to_highguardian_interaction_effect` and pointed it to `send_to_highguardian_interaction_effect_desc`.

- `common/character_memory_types/elf_maa_memory_types.txt`
  - Memory descriptions now reference `found_highguardian_memory_desc*` localization keys. (Left internal key `found_highguard_memory` as-is.)

- `common/decisions/elven_professionalism_decisions.txt`
  - Updated decision description and tooltip references to `found_highguardian_decision_desc`, `found_highguardian_decision_tooltip` and unlock tooltip `unlocked_highguardian_desc`.
  - Note: the decision block `found_highguard_decision` (internal id) was left as-is.

- `events/scheme_events/OVERRIDE_muder_scheme.txt`
  - Replaced `id = highguard.3001` → `id = highguardian.3001` and updated murder save death descriptions to use `murder_save.*.highguardian_dies` localization.

- `events/highguardian_events.txt`
  - Event ids/namespace continue to use `highguardian` and event references point to canonicalized localization keys.

- `events/OVERRIDE_single_combat_events.txt`
  - Uses single-combat localization keys `single_combat.0001.highguardian.*` and tooltip `single_combat.0001.tt.highguardian`.

- Other adjusted files: `common/scripted_effects/OVERRIDE_eryndar_court_position_effects.txt`, `common/court_positions/types/elf_maa_court_positions.txt`, `localization/english/ep3/eryndar_events_l_english.yml`, GUI reference `gui/elf_maa_texticons.gui` (texture path unchanged), `common/on_action/*` (ongoing highguardian on_actions preserved)

## Verification steps performed
- Repo scans for `highguardian` and `highguard` occurrences.
- Confirmed all dotted localization/event keys that should be `highguardian` were standardized.
- Ran a custom script `tools/find_missing_decision_localizations.py` to detect missing decision localization keys; results show several missing keys across the repository unrelated to `highguardian` changes (report below).

## Missing keys detected by `tools/find_missing_decision_localizations.py`
The checker reported missing localization keys referenced by decisions (these likely pre-existed in the codebase):
- (list of found missing keys appears in terminal output; they are not directly related to the `highguardian` change)

## Testing checklist for in-game verification
1. Start a CK3 session with the mod enabled; examine debug log for missing localization key warnings.
2. Execute the decision `Found the Highguard` in-game; verify decision description, confirm dialog, toast tooltip, and unlock text display correctly.
3. Use dynasty interaction `Send to the Highguard` and verify the interaction description, toast, and effect text are correct.
4. Trigger single-combat moves for `highguardian` trait interactions and confirm correct single-combat strings and tooltips.
5. Trigger the murder save scheme that leads to `highguardian.3001` and check localized death descriptions render correctly.

---

If you'd like, I can:
- Create a PR from `standardize/highguardian-keys` with this changelog as the PR description.
- Proceed with the deeper refactor to rename internal IDs (`highguard` → `highguardian`) (I will prepare a thorough plan and compatibility notes before applying).
- Run additional automated checks and fix any missing decision localizations (the script reported several missing keys; I can help add or re-point keys where it makes sense).

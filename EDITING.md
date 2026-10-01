# Customer Editing Guide — ever-after-bloom

Hand-painted watercolour storybook invitation featuring an animated wax seal video opener, couple portraits, multi-chapter love story, venue details, interactive lantern wishes, and calendar links.

---

## Normal Customer Changes

All routine customer edits are configured in:
→ `editable/wedding-data.js`

### 1. Couple Names & Initials
Edit `couple` in `editable/wedding-data.js`:
- `bride`: Bride's first name (e.g. `"Sreya"`)
- `groom`: Groom's first name (e.g. `"Prashanth"`)
- `initials`: Monogram text on seal and hero (e.g. `"S & P"`)

### 2. Wedding Date & Times
Edit in `editable/wedding-data.js`:
- `dateISO`: ISO timestamp string (`YYYY-MM-DDTHH:MM:SS+05:30`) used for calendar buttons & reminders
- `dateLabel`: Formatted date (e.g. `"Sunday, 14 February 2027"`)
- `timeLabel`: Formatted time (e.g. `"6:30 in the evening"`)
- `dressCode`: Dress code guidance (e.g. `"Festive Indian — pastels, ivory & gold"`)

### 3. Hero & Story
Edit in `editable/wedding-data.js`:
- `hero.kicker`: Opening line above couple names
- `hero.eyebrow`: Subtitle badge
- `hero.blessing`: Poetic blessing line
- `story.title` / `story.subtitle`: Section titles
- `story.bride`: Bride name, role, and story bio
- `story.groom`: Groom name, role, and story bio

### 4. Story Chapters
Edit `chapters` array in `editable/wedding-data.js`:
- Each item has `no` (e.g. `"I"`), `title`, `when`, and narrative `text`.

### 5. Venue & Map
Edit `venue` in `editable/wedding-data.js`:
- `name`: Palace or venue name
- `address`: Street address
- `mapsQuery`: Search term for Google Maps directions

### 6. Footer
Edit `footer` in `editable/wedding-data.js`:
- `line1`, `line2`, and `signoff` text

### 7. Images & Video
Replace files in `editable/assets/` or update paths in `wedding-data.js`:
- `seal`: Wax seal artwork (`invite-seal.png`)
- `openVideo`: Seal opening animation video (`invite-open.mp4`)
- `portraitBride` & `portraitGroom`: Couple watercolour portraits
- `heroPalace` & `gardenCourtyard`: Venue background artwork
- `mapPlate`: Illustrated map illustration
- `sceneDancing`, `sceneWalking`, etc.: Illustrated chapter scenes

---

## Rules for Future Agents

1. Make edits in `editable/wedding-data.js` and swap image files in `editable/assets/`.
2. Do not modify production files in `assets/` unless structural changes are requested.
3. Verify syntax with `node --check editable/wedding-data.js`.

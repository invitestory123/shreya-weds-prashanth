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

### 8. Social Preview (og:image, og:title, og:logo)

Meta tags live in the `<head>` of `index.html`:
- `og:title` / `twitter:title`: `Sreya & Prashanth — Two Cities, One Heart`
- `og:description`: one-line invitation summary (couple, date, venue)
- `og:url` / `canonical`: `https://sreya-weds-prashanth.invitestory.in/`
- `og:logo`: S&P monogram (`editable/assets/sp-monogram.png`)
- `og:image`: `editable/assets/og-image.jpg` (1200×630, absolute URL)

The OG card itself is hand-built in `editable/og-source.html` (ivory + gold, real
site fonts, S&P monogram, Victoria Memorial/Charminar crest). To regenerate after
a text change, render it headlessly and overwrite the jpg:

```
chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1200,630 --virtual-time-budget=9000 --screenshot=og.png \
  "file:///C:/invitestory/week5/shreya-weds-prashanth/editable/og-source.html"
```

Then downscale the PNG to 1200×630 and save as `editable/assets/og-image.jpg`
(quality ~93, ~115 KB). Non-ASCII text in `og-source.html` must be written as
HTML entities (`&#183;`, `&#2405;` ...) so the render never depends on charset.

---

## Rules for Future Agents

1. Make edits in `editable/wedding-data.js` and swap image files in `editable/assets/`.
2. Do not modify production files in `assets/` unless structural changes are requested.
3. Verify syntax with `node --check editable/wedding-data.js`.

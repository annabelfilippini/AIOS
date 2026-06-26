# Freeride Tarifa Instagram Originals Inventory

Date pulled: 2026-06-09
Source account: <https://www.instagram.com/freeridetarifa/>
Method: `gallery-dl` (photos) + `yt-dlp` (reels), authenticated via browser cookies.
Permission: Freeride consented to use of their content for the website refresh.
Location: `assets/instagram-originals/`

These are full-resolution originals, not screenshots. They replace the temporary
preview frames in `assets/instagram-collage/`. Total: 22 media files, ~89MB.

| Folder | Type | Files | Shows | Best website role |
| --- | --- | --- | --- | --- |
| `01-tarifa-lifestyle` | Reel | 1 mp4 | Tarifa lifestyle, kites, sun, ocean | Homepage motion moment / Options |
| `02-meet-oleg-instructor` | Reel | 1 mp4 | "Meet Oleg", instructor personality | Instructors section / social proof |
| `03-beginner-reassurance` | Reel | 1 mp4 | Tarifa is not only for pros | Lessons hero / supporting |
| `04-meet-lea-solo-traveler` | Reel | 1 mp4 | "Meet Lea", solo traveler camp story | Kite Camp / testimonial proof |
| `05-aerial-tarifa` | Photo | 3 jpg | Aerial Tarifa, beaches, water, kites | Location / homepage transition |
| `06-old-town-lifestyle` | Photo | 4 jpg | Tarifa old town, cafes, after-water | After kite / Location / Travel |
| `07-kite-camp-group` | Photo | 6 webp | Kite camp offer, group-trip framing | Kite Camp / homepage Options |
| `08-kite-yoga` | Photo | 1 jpg | Kite + yoga positioning | Kite & Yoga module |
| `09-process-laughs` | Reel | 1 mp4 | Process, laughs, friendly instruction | Lessons social proof |
| `10-all-levels-progression` | Photo | 3 jpg | All levels welcome, progression | Lessons / pricing support |

## Notes

- `.webp` files (folder 07) may need conversion to `.jpg`/`.png` for some
  pipelines. Convert on use, keep originals.
- Each folder also holds a `.json` sidecar with the post metadata (caption,
  date, dimensions) from `--write-metadata`.
- Reels were downloaded as merged mp4 (video + audio). Keep a still cover frame
  for every video section as a fallback per the design brief.
- Faces of identifiable students/guests (e.g. Lea) need usage permission before
  production. Confirm with Freeride which featured-guest images are cleared.

## How to re-pull or extend

```bash
# single post (photos + carousel)
gallery-dl --cookies-from-browser chrome -D <outdir> --write-metadata <post-url>

# single reel (video, more reliable than gallery-dl for video)
yt-dlp --cookies-from-browser chrome -o "<outdir>/%(id)s.%(ext)s" <reel-url>
```

Keep a 6-12s pause between posts to avoid Instagram 429 / login-redirect
rate-limiting. If a video CDN URL returns 429, retry that one via `yt-dlp`.

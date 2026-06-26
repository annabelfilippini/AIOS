# Dr. Joseph Feste CV Source Audit

Date: 2026-06-07
Supplied URL: <https://www.vitalhealthim.com/resume>

## Finding

The supplied Wix page is titled `RESUME | VitalHealthIM`. The server-rendered
HTML does not expose Dr. Feste's CV in visible page text or static links, but
the rendered browser page loads a client-side PDF viewer iframe from
`innotech-apps.com`.

The PDF viewer request contains the original file:

- File name: `Dr Feste CV.pdf`
- Source: Firebase Storage for `pdfwidget.appspot.com`
- PDF title: `CURRICULUM VITAE`
- Page count: 37
- First heading: `JOSEPH R. FESTE, M.D.`

The visible browser toolbar also confirms the viewer presents `1 / 37` pages.

## Local Project Context

The existing Vital Health review page had a placeholder link:

`Download Dr. Feste's CV`

The local meeting notes also say:

- `Add a placeholder "Download Dr. Feste's CV" link on his About bio.`
- `Replace Dr. Feste CV placeholder once they send the 55 page CV file.`

The live `/resume` page now provides the current 37-page CV via the embedded
viewer.

## Asset Created

Created a site-ready copy of the full CV:

- `assets/cv/dr-joseph-feste-cv.pdf`

Verified locally with `pdfinfo`: `Pages: 37`, letter page size, not encrypted.

## Recommendation

For the new site, link `assets/cv/dr-joseph-feste-cv.pdf` from Dr. Feste's About
bio using the label `Download Dr. Feste's CV`.

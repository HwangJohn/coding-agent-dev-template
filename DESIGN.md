---
version: alpha
name: Agentic Python Workbench
description: A restrained developer-tool design system for Python projects built with coding agents.
colors:
  primary: "#151A1F"
  secondary: "#3A6EA5"
  tertiary: "#2F8F6B"
  neutral: "#F5F7FA"
  surface: "#FFFFFF"
  surface-muted: "#E7ECF2"
  border: "#CCD6E0"
  text: "#151A1F"
  text-muted: "#5F6B7A"
  success: "#2F8F6B"
  warning: "#A66A00"
  error: "#B42318"
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: 0em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: 650
    lineHeight: 1.25
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0em
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0em
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  "2xl": 48px
  page-max: 1200px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 12px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    borderColor: "{colors.border}"
    padding: 12px
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    borderColor: "{colors.border}"
    padding: 24px
  code-block:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.code-md}"
    rounded: "{rounded.md}"
    padding: 16px
---

# Agentic Python Workbench

## Overview

This design system is for internal developer tools, documentation pages, status dashboards, and small web UIs that may be generated from this Python template. The interface should feel quiet, precise, and work-focused. It should prioritize scanning, comparison, and repeated action over marketing-style presentation.

For non-UI Python packages, do not force visual work into the project. Use this file only when generating a user interface, documentation site, dashboard, or design-facing artifact.

## Colors

The palette uses neutral surfaces with a dark ink primary and two functional accents.

- **Primary (#151A1F):** Main text, high-emphasis controls, code block backgrounds, and navigation anchors.
- **Secondary (#3A6EA5):** Informational highlights, links, selected states, and low-risk primary affordances.
- **Tertiary (#2F8F6B):** Success states, completed checks, and positive operational signals.
- **Neutral (#F5F7FA):** Page background for dense tools and documentation.
- **Surface (#FFFFFF):** Panels, tables, forms, and content regions.
- **Border (#CCD6E0):** Dividers and quiet component outlines.
- **Error (#B42318):** Destructive actions and failing validation states.

## Typography

Use Inter for interface text and JetBrains Mono for code, commands, identifiers, and terminal output. Typography should be compact and legible, with no negative letter spacing. Reserve `headline-lg` for top-level page titles only. Use `headline-md`, `body-sm`, and `label-md` inside panels, sidebars, tables, and forms.

## Layout

Use a maximum content width of 1200px for pages and a base spacing rhythm of 8px. Prefer dense but readable layouts: tables for comparison, sidebars for navigation, and full-width bands for major page regions. Avoid nested cards. Use panels only for bounded tools, repeated records, modals, or settings groups.

## Elevation & Depth

Use borders and tonal contrast instead of heavy shadows. Depth should be subtle: a panel can have a 1px border and surface background, while modals may add a light shadow only when separation from the page is necessary.

## Shapes

Use small radii. Buttons, inputs, panels, and code blocks default to 8px. Small controls can use 4px. Pills and avatars may use `full`, but avoid large rounded rectangles as decorative elements.

## Components

Buttons should use icon-only or icon-and-text treatment when the action is common and recognizable. Primary buttons are dark and reserved for the main action in a view. Secondary buttons are outlined and used for routine actions. Inputs should have visible labels, clear focus states, and inline validation. Tables should support dense scanning with stable row height, clear column labels, and subdued dividers. Code blocks should use the dark primary background with high-contrast text.

## Do's and Don'ts

- Do use `DESIGN.md` when creating UI, dashboards, documentation sites, or generated visual assets.
- Do keep operational screens quiet, structured, and fast to scan.
- Do maintain WCAG AA contrast for text and controls.
- Do use borders, spacing, and typography for hierarchy before adding shadows.
- Don't use purple-blue gradient hero sections, decorative blobs, or generic SaaS landing-page composition.
- Don't create nested cards or oversized type inside compact tool surfaces.
- Don't use this file as the software architecture document; use `AGENTS.md` and ADRs for that.

# Custom Frame Art Library

This folder contains custom frame art that will be applied to ALL Proxyshop templates during rendering.

## Folder Structure

```
art/custom-frames/
├── borders/              # Frame borders and outer elements
├── textboxes/            # Rules text background elements  
├── title-boxes/          # Name/title area elements
├── pinlines/             # Color identity accent lines
└── pt-boxes/             # Power/toughness boxes
```

## File Naming Convention

Files should be named using this simple pattern:
`{element-name}.{extension}`

Examples:
- `border.png`
- `textbox.png`
- `pinlines.png`
- `pt-box.png`

## Usage

**One frame style for everything** - all cards will use identical frame elements regardless of:
- Card color identity
- Card type (creature, spell, etc.)
- Template variant (showcase, classic, etc.)

The Frame Replacement Automation plugin will automatically apply these elements to every card during rendering. 
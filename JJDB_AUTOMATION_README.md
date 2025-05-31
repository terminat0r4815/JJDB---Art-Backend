# JJDB Custom Frame Automation System

## 🎯 Project Overview

This system automates the replacement of Magic: The Gathering card frame elements in Proxyshop PSD templates with custom JJDB-style graphics. It enables universal frame design across all card types and colors while maintaining Proxyshop compatibility.

## 📁 Project Structure

```
JJDB/Proxyshop - latest release/
├── 📄 jjdb_artlayer_fixed.py          # ✅ MAIN AUTOMATION SCRIPT
├── 📄 JJDB_AUTOMATION_README.md       # 📖 This documentation
├── 📁 venv_jjdb/                      # 🐍 Python 3.12 virtual environment
├── 📁 plugins/JJDB/                   # 🔌 Proxyshop plugin
│   ├── 📄 manifest.yml                # Plugin configuration
│   ├── 📄 README.md                   # Plugin documentation
│   └── 📁 py/                         # Python template code
├── 📁 art/custom-frames/               # 🎨 Custom frame graphics
│   ├── 📁 borders/border.png           # Card borders
│   ├── 📁 textboxes/textbox.png        # Rules text backgrounds
│   ├── 📁 title-boxes/title-box.png   # Name/title backgrounds
│   ├── 📁 pinlines/pinlines.png        # Decorative accents
│   └── 📁 pt-boxes/pt-box.png         # Power/toughness boxes
├── 📁 templates/normal.psd             # 🖼️ Main template file
└── 📁 templates_backup/                # 💾 Backup of original templates
```

## 🎊 SUCCESS STATUS

### ✅ **FULLY WORKING AUTOMATION**
- **Layer Detection**: Finds all 100+ color-specific sublayers ✓
- **Frame Mapping**: Correctly maps each layer type to its custom PNG ✓  
- **Content Replacement**: Successfully replaces layer content ✓
- **Proxyshop Compatibility**: Preserves layer names and structure ✓

### 🎯 **Key Achievements**
- Universal design works for ALL card types and colors
- Python 3.12 virtual environment with working dependencies
- Comprehensive layer group and sublayer detection
- Proper frame file mapping (PT boxes get pt-box.png, borders get border.png, etc.)
- Safe testing mode with rollback capability

## 🚀 Quick Start Guide

### Prerequisites
1. **Photoshop** installed and running
2. **Python 3.12** virtual environment activated
3. **Custom frame PNG files** in correct directories
4. **templates/normal.psd** open in Photoshop

### Run Automation
```powershell
# Activate virtual environment
.\\venv_jjdb\\Scripts\\Activate.ps1

# Run the automation script
python jjdb_artlayer_fixed.py
```

### Interactive Process
1. **File Check**: Script verifies all custom PNG files exist
2. **Test Mode**: Replace 3 PT Box layers to verify functionality  
3. **Full Mode**: Replace all 100+ layers across all frame types
4. **Auto-Save**: Document saved automatically after completion

## 🔧 Technical Implementation

### **Core Technology Stack**
- **Language**: Python 3.12
- **API**: `photoshop-python-api` for COM interface
- **Method**: Copy/paste replacement (most reliable)
- **Architecture**: Layer group traversal with individual file mapping

### **Frame Type Detection**
```python
# Layer path examples and their mappings:
"PT Box/W" → pt-boxes/pt-box.png
"Background/Blue" → borders/border.png  
"Name & Title Boxes/R" → title-boxes/title-box.png
"Pinlines & Textbox/G" → pinlines/pinlines.png
```

### **Replacement Process**
1. **Layer Selection**: Use COM API to select specific sublayer
2. **Content Clearing**: `selectAll()` → `clear()` existing content
3. **PNG Loading**: Open custom frame PNG in Photoshop
4. **Content Copy**: Copy all content from PNG document
5. **Content Paste**: Paste into target layer
6. **Cleanup**: Close PNG, deselect, move to next layer

## 📊 Layer Structure Analysis

### **Detected Layer Groups** (20 total)
- **PT Box** - Power/toughness frame elements
- **Background** - Main card border frames  
- **Name & Title Boxes** - Card name area frames
- **Pinlines & Textbox** - Rules text area frames
- **Type Line** - Card type area frames
- *...and 15 other specialized frame groups*

### **Color Variants** (per group)
Each frame group contains sublayers for:
- **WUBRG**: White, Blue, Black, Red, Green
- **Special**: Gold, Artifact, Colorless, Land, Vehicle
- **Total**: ~117 individual sublayers requiring replacement

## 🎨 Custom Frame Requirements

### **File Structure**
```
art/custom-frames/
├── borders/border.png           # Universal card border
├── textboxes/textbox.png        # Rules text background  
├── title-boxes/title-box.png   # Name area background
├── pinlines/pinlines.png        # Decorative elements
└── pt-boxes/pt-box.png         # Power/toughness box
```

### **Design Specifications**
- **Format**: PNG with transparency
- **Approach**: Universal design (same frame for all colors)
- **Resolution**: Match PSD layer dimensions
- **Style**: JJDB aesthetic with clean, modern lines

## 🔄 Development History

### **Challenges Overcome**
1. **Python 3.13 Compatibility** → Created Python 3.12 virtual environment
2. **Smart Object Errors** → Switched to copy/paste method
3. **Wrong File Mapping** → Implemented proper frame type detection
4. **Layer Access Issues** → Used layerSets API for sublayer access
5. **COM Interface** → Extensive API research and testing

### **Script Evolution**
- `automate_jjdb_frames.py` → Initial attempt (ActionDescriptor approach)
- `automate_jjdb_frames_v2.py` → Added layer group detection
- `automate_jjdb_frames_v3.py` → Comprehensive sublayer enumeration
- `jjdb_ultimate_solution.py` → Research-based smart object approach
- `jjdb_artlayer_fixed.py` → **✅ WORKING SOLUTION** (copy/paste method)

## 📋 Future Development

### **Potential Enhancements**
1. **GUI Interface** - Visual layer selection and preview
2. **Batch Processing** - Multiple PSD files at once  
3. **Frame Variants** - Support for different frame styles per card type
4. **Undo System** - Granular rollback of individual layers
5. **Performance** - Optimize for large template files

### **Code Maintenance**
- **Virtual Environment**: Keep Python 3.12 for compatibility
- **API Dependencies**: Monitor `photoshop-python-api` updates
- **Backup System**: Always backup PSD before automation
- **Testing**: Verify with each Photoshop/Proxyshop update

### **Extension Ideas**
- **Custom Watermarks** - Add set symbols or artist signatures
- **Foil Effects** - Automated foil layer generation
- **Card Type Variants** - Different frames for creatures vs spells
- **Quality Control** - Automated checking of frame alignment

## 🛡️ Safety & Backup

### **Built-in Safety Features**
- **Test Mode**: Always test with 3 layers before full replacement
- **File Validation**: Verifies all PNG files exist before starting
- **Error Handling**: Graceful failure with detailed error messages
- **Progress Tracking**: Shows exactly which layers succeeded/failed

### **Manual Backup Procedure**
```powershell
# Before running automation:
copy "templates/normal.psd" "templates/normal_backup_YYYYMMDD.psd"
```

### **Recovery Process**
If automation fails or produces unexpected results:
1. Close modified PSD without saving
2. Restore from `templates_backup/` or manual backup
3. Check PNG file integrity and paths
4. Re-run automation with test mode

## 📞 Support & Troubleshooting

### **Common Issues**
- **"No module named photoshop"** → Activate virtual environment
- **"No active document"** → Open normal.psd in Photoshop first
- **"File not found"** → Check custom frame PNG paths
- **"Layer selection failed"** → Ensure PSD layer structure is intact

### **Debug Information**
The script provides comprehensive debugging output:
- File path verification
- Layer detection results  
- Frame file mapping
- Step-by-step replacement progress

### **Contact**
For technical issues or enhancement requests, refer to this README and the working script comments for implementation details.

---

## 🎉 Project Status: **COMPLETE & WORKING**

The JJDB custom frame automation system is **fully functional** and ready for production use. The universal frame approach successfully replaces all Magic card frame elements while maintaining full Proxyshop compatibility.

**Last Updated**: Based on successful automation testing with 100+ layer replacements
**Status**: ✅ Production Ready
**Maintainer**: JJDB Custom Frames Project 
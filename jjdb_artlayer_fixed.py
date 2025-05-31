#!/usr/bin/env python3
"""
JJDB Art Layer Solution - FIXED VERSION
Fixes the file path issues and adds proper debugging.
"""

import os
import sys
import time
from pathlib import Path

try:
    import photoshop.api as ps
    print("✅ Connected via photoshop-python-api")
except Exception as e:
    print(f"❌ Cannot connect to Photoshop API: {e}")
    sys.exit(1)

class JJDBArtLayerFixed:
    """Fixed solution with proper file paths."""
    
    def __init__(self):
        self.app = ps.Application()
        self.frames_path = Path("art/custom-frames")
        
    def debug_file_paths(self):
        """Check what files actually exist."""
        print("🔍 DEBUGGING FILE PATHS:")
        print("-" * 40)
        
        # Check current working directory
        cwd = Path.cwd()
        print(f"📁 Current directory: {cwd}")
        
        # Check frames path
        frames_abs = self.frames_path.resolve()
        print(f"📁 Frames path: {frames_abs}")
        print(f"📁 Frames exists: {frames_abs.exists()}")
        
        if frames_abs.exists():
            print("\n📋 Available frame files:")
            for subdir in ["borders", "textboxes", "title-boxes", "pinlines", "pt-boxes"]:
                subdir_path = frames_abs / subdir
                if subdir_path.exists():
                    print(f"  📁 {subdir}/")
                    for file in subdir_path.glob("*.png"):
                        print(f"    📄 {file.name} → {file}")
                else:
                    print(f"  ❌ {subdir}/ (not found)")
        
        print("-" * 40)
    
    def get_working_frame_file(self, layer_path):
        """Get the CORRECT frame file based on layer path."""
        layer_path_lower = layer_path.lower()
        
        # Determine the correct frame type based on the layer path
        if "pt box" in layer_path_lower:
            frame_file = self.frames_path / "pt-boxes" / "pt-box.png"
            frame_type = "PT Box"
        elif "background" in layer_path_lower:
            frame_file = self.frames_path / "borders" / "border.png"
            frame_type = "Background/Border"
        elif "name & title" in layer_path_lower:
            frame_file = self.frames_path / "title-boxes" / "title-box.png"
            frame_type = "Title Box"
        elif "pinlines" in layer_path_lower:
            frame_file = self.frames_path / "pinlines" / "pinlines.png"
            frame_type = "Pinlines"
        elif "textbox" in layer_path_lower:
            frame_file = self.frames_path / "textboxes" / "textbox.png"
            frame_type = "Textbox"
        else:
            # Default to border for unknown types
            frame_file = self.frames_path / "borders" / "border.png"
            frame_type = "Default (Border)"
        
        abs_path = frame_file.resolve()
        
        if abs_path.exists():
            print(f"  📄 Using {frame_type} file: {abs_path}")
            return abs_path
        else:
            print(f"  ❌ {frame_type} file not found: {abs_path}")
            # Fallback to any working file
            possible_files = [
                self.frames_path / "borders" / "border.png",
                self.frames_path / "textboxes" / "textbox.png", 
                self.frames_path / "title-boxes" / "title-box.png",
                self.frames_path / "pinlines" / "pinlines.png",
                self.frames_path / "pt-boxes" / "pt-box.png"
            ]
            
            for fallback_file in possible_files:
                fallback_abs = fallback_file.resolve()
                if fallback_abs.exists():
                    print(f"  📄 Using fallback file: {fallback_abs}")
                    return fallback_abs
            
            print(f"  ❌ NO WORKING FILES FOUND!")
            return None
    
    def simple_replace_content(self, layer, png_file_path, layer_path):
        """Simple method - just use copy/paste."""
        print(f"\n🔧 Replacing {layer_path}...")
        print(f"  📁 Source file: {png_file_path}")
        print(f"  📄 File exists: {png_file_path.exists()}")
        
        if not png_file_path.exists():
            print(f"  ❌ File doesn't exist, skipping")
            return False
        
        try:
            # Set active layer
            self.app.activeDocument.activeLayer = layer
            print(f"  ✅ Set active layer: {layer.name}")
            
            # Clear current content
            self.app.activeDocument.selection.selectAll()
            self.app.activeDocument.selection.clear()
            print(f"  ✅ Cleared existing content")
            
            # Open the PNG file
            png_doc = self.app.open(str(png_file_path))
            print(f"  ✅ Opened PNG file")
            
            # Copy all content from PNG
            png_doc.selection.selectAll()
            png_doc.selection.copy()
            print(f"  ✅ Copied PNG content")
            
            # Close PNG
            png_doc.close()
            print(f"  ✅ Closed PNG file")
            
            # Switch back to main document and paste
            self.app.activeDocument.activeLayer = layer
            self.app.activeDocument.paste()
            print(f"  ✅ Pasted content into layer")
            
            # Deselect
            self.app.activeDocument.selection.deselect()
            print(f"  ✅ SUCCESS: {layer_path}")
            return True
            
        except Exception as e:
            print(f"  ❌ FAILED: {e}")
            return False
    
    def run_test_replacement(self):
        """Test with just a few layers first."""
        print("🧪 JJDB TEST REPLACEMENT")
        print("=" * 60)
        
        # Debug file paths first
        self.debug_file_paths()
        
        # Check active document
        try:
            doc = self.app.activeDocument
            print(f"✅ Active document: {doc.name}")
        except Exception as e:
            print(f"❌ No active document: {e}")
            return False
        
        # Find first few PT Box layers for testing
        test_layers = []
        
        def find_test_layers(container, path=""):
            for layer_set in container.layerSets:
                set_path = f"{path}/{layer_set.name}" if path else layer_set.name
                if "pt box" in set_path.lower():
                    for art_layer in layer_set.artLayers:
                        if len(test_layers) < 3:  # Only test 3 layers
                            layer_path = f"{set_path}/{art_layer.name}"
                            test_layers.append({
                                'layer': art_layer,
                                'path': layer_path
                            })
                find_test_layers(layer_set, set_path)
        
        find_test_layers(doc)
        
        if not test_layers:
            print("❌ No test layers found!")
            return False
        
        print(f"\n🧪 Testing with {len(test_layers)} layers:")
        for layer_info in test_layers:
            print(f"  📄 {layer_info['path']}")
        
        # Confirm
        response = input(f"\n🤔 Test replace {len(test_layers)} layers? (y/n): ").strip().lower()
        if response != 'y':
            print("❌ Cancelled")
            return False
        
        # Execute test replacements
        print(f"\n🔧 EXECUTING TEST REPLACEMENTS:")
        print("-" * 40)
        
        success_count = 0
        for i, layer_info in enumerate(test_layers, 1):
            layer = layer_info['layer']
            layer_path = layer_info['path']
            
            print(f"\n[{i}/{len(test_layers)}] Testing {layer_path}...")
            
            # Get the correct frame file for this specific layer
            frame_file = self.get_working_frame_file(layer_path)
            if not frame_file:
                print(f"  ❌ No frame file found for {layer_path}")
                continue
            
            if self.simple_replace_content(layer, frame_file, layer_path):
                success_count += 1
            
            time.sleep(0.5)  # Pause to see results
        
        # Results
        print(f"\n🎉 TEST COMPLETE!")
        print(f"✅ Successfully replaced: {success_count}/{len(test_layers)} layers")
        
        if success_count > 0:
            print("\n🎊 SUCCESS! The replacement is working!")
            print("You should see custom frames in the test layers.")
            
            # Ask if they want to do all layers
            response = input("\n🤔 Replace ALL 132 layers? (y/n): ").strip().lower()
            if response == 'y':
                return self.run_full_replacement()
        else:
            print("\n❌ Test failed. Check the file paths and try again.")
        
        return success_count > 0
    
    def run_full_replacement(self):
        """Replace all layers with the working file."""
        print("\n🚀 FULL REPLACEMENT MODE")
        print("=" * 60)
        
        # Find all replaceable layers (simplified)
        all_layers = []
        doc = self.app.activeDocument
        
        def find_all_layers(container, path=""):
            for layer_set in container.layerSets:
                set_path = f"{path}/{layer_set.name}" if path else layer_set.name
                # Check if this is a frame group
                if any(group in set_path.lower() for group in ['pt box', 'background', 'pinlines', 'name & title']):
                    for art_layer in layer_set.artLayers:
                        layer_path = f"{set_path}/{art_layer.name}"
                        # Check if this is a color layer
                        if art_layer.name.lower() in ['w', 'u', 'b', 'r', 'g', 'gold', 'artifact', 'colorless', 'land']:
                            all_layers.append({
                                'layer': art_layer,
                                'path': layer_path
                            })
                find_all_layers(layer_set, set_path)
        
        find_all_layers(doc)
        
        print(f"🔍 Found {len(all_layers)} layers to replace")
        
        success_count = 0
        for i, layer_info in enumerate(all_layers, 1):
            layer = layer_info['layer']
            layer_path = layer_info['path']
            
            print(f"[{i}/{len(all_layers)}] {layer_path}...")
            
            # Get the correct frame file for this specific layer
            frame_file = self.get_working_frame_file(layer_path)
            if not frame_file:
                print(f"  ❌ No frame file found for {layer_path}")
                continue
            
            if self.simple_replace_content(layer, frame_file, layer_path):
                success_count += 1
            
            if i % 10 == 0:  # Progress update every 10 layers
                print(f"📊 Progress: {i}/{len(all_layers)} ({success_count} successful)")
        
        # Save
        print(f"\n💾 Saving document...")
        doc.save()
        
        print(f"\n🎉 FULL REPLACEMENT COMPLETE!")
        print(f"✅ Successfully replaced: {success_count}/{len(all_layers)} layers")
        
        return success_count > 0

def main():
    print("JJDB Art Layer Solution - FIXED VERSION")
    print("Fixes file path issues and adds debugging\n")
    
    print("📋 INSTRUCTIONS:")
    print("1. Open templates/normal.psd in Photoshop")
    print("2. Make sure it's the active document") 
    print("3. Run this script for testing\n")
    
    replacer = JJDBArtLayerFixed()
    success = replacer.run_test_replacement()
    
    if success:
        print("\n✅ Solution working!")
    else:
        print("\n❌ Needs attention.")
    
    return success

if __name__ == "__main__":
    main() 
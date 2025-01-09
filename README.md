# **Image Annotation**

This repository provides a Python script for annotating images using OpenCV. The script demonstrates how to:

- Draw rectangles on an image.
- Apply semi-transparency (alpha blending) to specific regions.
- Add text annotations using OpenCV's built-in fonts.

## **Features**
- **Green Rectangle**: Solid rectangle drawn around a region of interest.
- **Black Rectangle**: Semi-transparent background for text.
- **Text Annotation**: Text added on top of the black rectangle.

## **Usage**

### **Using Conda**
1. Clone the repository:
   ```bash
   git clone https://github.com/yvesHakizimana/open-cv-workflow.git
   cd open-cv-workflow
   ```

2. Create a new Conda environment:
   ```bash
   conda create --name image_annotation_env python=3.8
   conda activate image_annotation_env
   ```

3. Install required dependencies:
   ```bash
   pip install opencv-python
   ```

### **Using Jupyter Notebook**
1. Install Jupyter in your Conda environment:
   ```bash
   conda install -c conda-forge notebook
   ```

2. Open Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Add the code to a new notebook cell and run it. Ensure the input image is in the same directory.

### **Using PyCharm**
1. Open the repository folder in PyCharm.
2. Configure the interpreter:
   - Go to **File > Settings > Project: <ProjectName> > Python Interpreter**.
   - Select the Conda environment you created.
3. Run the notebook (`open-cv.ipynb`) using PyCharm's Run feature.

## **Requirements**
- Python 3.7 or higher
- Required library:
  - OpenCV

## **File Structure**
```
.
├── assignment-001-given.jpg # Input image
├── open-cv.ipynb              # Main Python script
├── output.jpg               # Annotated output image
```

## **Output**
- The script displays the annotated image and saves it as `output.jpg` in the current directory.

## **License**
This project is open-source and available under the [MIT License](LICENSE).

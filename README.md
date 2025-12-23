# 🚀 Enterprise Risk Management Toolset

A comprehensive, interactive web-based platform for Enterprise Risk Management (ERM) workflows, including risk assessment, control mapping, RCM generation, audit program creation, and advanced analytics.

## ✨ Features

### 🎯 Core Functionality
- **Risk & Control Management**: Import and manage risks and controls from CSV/Excel files
- **RCM Generation**: Automated Risk & Control Matrix creation with gap analysis
- **Audit Program Builder**: Generate comprehensive audit programs with testing procedures
- **Process Flow Visualization**: Create and analyze business process flows
- **Multi-Format Support**: Parse PDF, Word, Excel, CSV, images, and text files

### 📊 Advanced Analytics
- **Risk Heat Maps**: Interactive likelihood × impact matrix visualization
- **Dashboard Analytics**: Risk distribution, control coverage, and trend analysis
- **Chart.js Integration**: Beautiful, interactive charts and graphs
- **Real-time Statistics**: Live counting and updates as data changes

### 📝 Templates & Reports
- **Standardized Templates**: Download pre-formatted CSV/Excel templates
- **Template Validation**: Built-in validation for data imports
- **Audit Report Generator**: Create professional Word documents with findings
- **Export Capabilities**: Export to Excel, Word, HTML, and custom .erm formats

### 👥 Collaboration Features
- **Project Management**: Track project status, ownership, and progress
- **Comments System**: Add reviews and comments to risks and controls
- **Project Export/Import**: Share complete projects with team members
- **Version Control**: Track changes and maintain project history

## 🌐 Live Demo

**🔗 [Try it now!](https://[YOUR-USERNAME].github.io/erm-toolset/erm_advanced.html)**

## 🚀 Quick Start

### Option 1: Use Online (No Installation)
Simply open the live demo link above and start using the tool immediately!

### Option 2: Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/[YOUR-USERNAME]/erm-toolset.git
   cd erm-toolset
   ```

2. Open `erm_advanced.html` in your web browser:
   ```bash
   # Windows
   start erm_advanced.html
   
   # macOS
   open erm_advanced.html
   
   # Linux
   xdg-open erm_advanced.html
   ```

### Option 3: Run with Python Backend (Optional)
For advanced features that require server-side processing:

1. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

3. Open `erm_advanced.html` in your browser

## 📖 Usage Guide

### 1. Load Data
- **Quick Start**: Click "Load Sample Data" to see the tool in action
- **Import Your Data**: Upload CSV/Excel files with risk and control information
- **Use Templates**: Download standardized templates from the Templates tab

### 2. Generate RCM
- Upload both risk and control data
- Click "Generate RCM + Audit Program"
- View the automatically generated Risk & Control Matrix

### 3. View Analytics
- Switch to the "Analytics Dashboard" tab
- Explore risk heat maps, distribution charts, and coverage metrics
- Interactive charts update automatically as you add data

### 4. Create Reports
- Navigate to "Report Generator" tab
- Configure report settings (audit name, auditor, date)
- Generate professional Word documents or HTML reports

### 5. Collaborate
- Set project information in the "Collaboration" tab
- Export complete projects as .erm files
- Share with team members for collaborative work

## 📁 File Structure

```
erm-toolset/
├── erm_advanced.html          # Main advanced platform (recommended)
├── erm_complete.html          # Complete integrated workflow
├── index.html                 # Landing page
├── multi_format_demo.html     # Multi-format file parser demo
├── erm_toolset.py            # Python library for ERM functions
├── sample_risks.csv           # Sample risk data
├── sample_controls.csv        # Sample control data
├── template_risks.csv         # Risk import template
├── template_controls.csv      # Control import template
├── requirements.txt           # Python dependencies
└── backend/                   # Optional Python backend
    ├── main.py               # FastAPI server
    └── requirements.txt      # Backend dependencies
```

## 🎨 Technologies Used

### Frontend
- **HTML5 & CSS3**: Modern, responsive design
- **Vanilla JavaScript**: No framework dependencies
- **Chart.js**: Interactive data visualizations
- **SheetJS (xlsx)**: Excel file processing
- **FileSaver.js**: File download functionality
- **Docxtemplater**: Word document generation

### Backend (Optional)
- **Python 3.9+**
- **FastAPI**: Modern, fast web framework
- **Pandas**: Data manipulation
- **python-docx**: Document generation

### Design
- **Inter Font**: Professional typography
- **Glassmorphism**: Modern UI effects
- **Dark Theme**: Eye-friendly interface
- **Gradient Accents**: Premium visual appeal

## 🌟 Key Features

### Workflow Tab
- Integrated workflow from risk input to audit program generation
- Real-time statistics dashboard
- Quick upload with sample data support

### Analytics Dashboard
- **Risk Heat Map**: Likelihood × Impact matrix with color coding
- **Risk Distribution**: Pie chart by category
- **Control Coverage**: Doughnut chart showing gaps
- **Risk Ratings**: Bar chart of severity levels
- **Control Types**: Analysis of preventive, detective, corrective controls

### Templates & Import
- Download standardized CSV/Excel templates
- Validation on import with error reporting
- Instructions included in Excel templates
- Support for multiple Risk IDs per control

### Report Generator
- Professional audit report generation
- Customizable sections (Executive Summary, Findings, Appendices)
- Word and HTML export formats
- Configurable audit metadata

### Collaboration
- Project metadata tracking
- Export/Import complete projects
- Comments and review system
- Status tracking (Planning, In Progress, Review, Completed)

## 🤝 Contributing

Contributions are welcome! This is a demonstration project showcasing modern web development for enterprise applications.

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 🆘 Support

For questions or issues:
1. Check the built-in help tooltips in the application
2. Review the sample data for formatting examples
3. Download and review the templates for proper data structure

## 🎯 Use Cases

- **Internal Audit Teams**: Streamline audit planning and execution
- **Risk Managers**: Centralized risk and control documentation
- **Compliance Officers**: Track regulatory compliance controls
- **Audit Committees**: Visual dashboards for governance oversight
- **Consultants**: Professional deliverables for client engagements

---

**Made with ❤️ for auditors and risk professionals**

*Enterprise Risk Management made simple, visual, and collaborative.*

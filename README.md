# Static-Site-Generator

A simple, lightweight Static Site Generator that converts Markdown files into HTML pages. It uses customizable templates and requires minimal configuration, making it ideal for developers who want to quickly generate static websites.

## 🚀 Features

- Converts Markdown files into static HTML pages
- Easy-to-use command-line interface
- Customizable templates for flexible design
- Supports adding metadata to pages (e.g., title, author, date)
- Output is static HTML, ready for deployment anywhere

## ⚡ Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/VivaanTakodra/Static-Site-Generator.git
cd Static-Site-Generator
npm install
```

## 📋 Usage

1. Add your Markdown files to the `content` directory. Each file should have a `.md` extension and represent a page.
2. Create or modify your templates in the `templates` directory. The templates should use [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) syntax for dynamic content rendering.
3. Configure the site by editing the `config.json` file.
4. To generate the static site, run:

```bash
node generate.js
```

This will generate static HTML files inside the `output` directory.

## 🛠️ Configuration

The `config.json` file allows you to configure various settings for your site. Here are the options available:

- **title**: The title of your site (e.g., "My Static Site").
- **author**: The author's name (e.g., "Vivaan Takodra").
- **theme**: The theme/template used for the site (e.g., "default").
- **outputDirectory**: The directory where the generated HTML files will be saved (default is `output`).

### Example `config.json`:

```json
{
  "title": "My Static Site",
  "author": "Vivaan Takodra",
  "theme": "default",
  "outputDirectory": "output"
}
```

## 📁 Folder Structure

Here's an overview of the folder structure:

```
Static-Site-Generator/
├── content/             # Markdown content files
├── templates/           # Jinja2 templates for rendering HTML
├── output/              # Generated HTML files
├── config.json          # Configuration file for the site
├── generate.js          # The main script to generate the site
└── package.json         # Project dependencies
```

## 📝 Contributing

We welcome contributions to this project! If you'd like to help improve the Static Site Generator, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and add tests (if applicable).
4. Open a pull request, describing your changes.

Please make sure to follow the existing code style and add tests for new features or bug fixes.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

### Key Sections:
- **Features**: Lists the main functionalities of the Static Site Generator.
- **Installation**: Provides installation instructions for the project.
- **Usage**: Describes how to use the generator with the content and templates.
- **Configuration**: Explains the `config.json` file settings and provides an example.
- **Folder Structure**: Gives an overview of the directory structure.
- **Contributing**: Explains how to contribute to the project.
- **License**: Details the licensing information.

This version includes all the sections and details you requested, formatted properly to work directly in a `README.md` file. You can paste this into your repository, and it will display nicely on GitHub.

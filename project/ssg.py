import os
import markdown
import yaml
import argparse
from jinja2 import Environment, FileSystemLoader
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Default paths
INPUT_DIR = "input"
OUTPUT_DIR = "output"
TEMPLATE_DIR = "templates"

# Initialize Jinja2 Environment
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def load_template(template_name):
    """Load an HTML template."""
    try:
        return env.get_template(template_name)
    except Exception as e:
        raise FileNotFoundError(f"Template '{template_name}' not found in {TEMPLATE_DIR}: {e}")


def convert_markdown_to_html(md_content):
    """Convert Markdown content to HTML."""
    return markdown.markdown(md_content)


def parse_metadata_and_content(md_content):
    """Extract YAML metadata and Markdown content."""
    if md_content.startswith("---"):
        _, yaml_block, md_body = md_content.split("---", 2)
        metadata = yaml.safe_load(yaml_block)
        return metadata, md_body
    return {}, md_content


def generate_html_page(template, content, metadata):
    """Generate an HTML page using the template and content."""
    return template.render(content=content, metadata=metadata)


def process_markdown_files(input_dir, output_dir, template_name):
    """Process all Markdown files in the input directory."""
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the specified template
    template = load_template(template_name)

    # Process each Markdown file
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_path = os.path.join(input_dir, filename)
            with open(input_path, "r", encoding="utf-8") as file:
                md_content = file.read()

            # Parse metadata and Markdown content
            metadata, md_body = parse_metadata_and_content(md_content)

            # Convert Markdown to HTML
            html_content = convert_markdown_to_html(md_body)

            # Generate the final HTML page
            output_html = generate_html_page(template, html_content, metadata)

            # Write the HTML file
            output_file = os.path.join(output_dir, filename.replace(".md", ".html"))
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(output_html)

            print(f"Generated: {output_file}")


def serve_output_directory(output_dir, port):
    """Serve the output directory using a simple HTTP server."""
    os.chdir(output_dir)
    server = HTTPServer(("localhost", port), SimpleHTTPRequestHandler)
    print(f"Serving at http://localhost:{port}")
    server.serve_forever()


def main():
    """Main function to handle CLI and process files."""
    parser = argparse.ArgumentParser(description="Static Site Generator")
    parser.add_argument("-i", "--input", default=INPUT_DIR, help="Input directory containing Markdown files")
    parser.add_argument("-o", "--output", default=OUTPUT_DIR, help="Output directory for generated HTML files")
    parser.add_argument("-t", "--template", default="base.html", help="Template file to use for HTML generation")
    parser.add_argument("-p", "--preview", action="store_true", help="Serve output directory for live preview")
    parser.add_argument("--port", type=int, default=8000, help="Port for the live preview server")
    args = parser.parse_args()

    try:
        process_markdown_files(args.input, args.output, args.template)
        if args.preview:
            serve_output_directory(args.output, args.port)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

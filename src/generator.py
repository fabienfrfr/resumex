import sqlite3
from jinja2 import Template
from weasyprint import HTML

def generate_cv(consultant_id):
    # Connect to local database
    conn = sqlite3.connect('data/resumex.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, expertise, bio FROM consultants WHERE id=?', (consultant_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        # Load template and render
        with open('src/template.html', 'r') as f:
            template = Template(f.read())
        
        rendered_html = template.render(name=row[0], expertise=row[1], bio=row[2])
        
        # Output PDF
        output_filename = f"CV_{row[0].replace(' ', '_')}.pdf"
        HTML(string=rendered_html).write_pdf(output_filename)
        print(f"✅ Success: {output_filename} generated.")
    else:
        print("❌ Error: Consultant not found.")

if __name__ == "__main__":
    # Change ID based on your database record
    generate_cv(1)
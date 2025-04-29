import pytest
from datetime import datetime
import os
import coverage

def pytest_html_report_title(report):
    report.title = "Laporan Pengujian Kalkulator"

def pytest_configure(config):
    # Add environment info to the report
    if hasattr(config, '_metadata'):
        config._metadata['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        config._metadata['Project'] = 'Kalkulator Sederhana'
        config._metadata['Python'] = pytest.__version__
        # Remove unwanted environment variables from report
        if 'JAVA_HOME' in config._metadata:
            del config._metadata['JAVA_HOME']
    else:
        # For newer pytest versions that handle metadata differently
        config.stash['metadata'] = {
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Project': 'Kalkulator Sederhana',
            'Python Version': pytest.__version__
        }

def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')
    cells.pop()  # Remove the links column

def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{getattr(report, "description", "")}</td>')
    cells.pop()  # Remove the links column

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # Get docstring from test function to use as description
    test_doc = item.obj.__doc__ or "No description provided"
    report.description = test_doc.strip()

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """Add coverage info to the summary section of the report"""
    try:
        from coverage import Coverage
        cov = Coverage()
        
        if os.path.exists('.coverage'):
            cov.load()
            
            # Create coverage data table for summary
            prefix.extend([
                '<div class="coverage-summary">',
                '<h2>Coverage Summary</h2>',
                '<table class="coverage-table">',
                '<tr><th>File</th><th>Statements</th><th>Missing</th><th>Coverage</th></tr>'
            ])
            
            # Add coverage data
            total_statements = 0
            total_missed = 0
            
            # Add rows for each file
            for filename in sorted(cov.get_data().measured_files()):
                rel_filename = os.path.relpath(filename)
                # analysis returns a tuple of (statements, excluded, missing, errors)
                analysis = cov.analysis(filename)
                statements = len(analysis[0])
                missing = len(analysis[2])
                
                covered = statements - missing
                total_statements += statements
                total_missed += missing
                
                if statements > 0:
                    percentage = (covered / statements) * 100
                    
                    # Determine coverage class for coloring
                    if percentage >= 80:
                        coverage_class = 'high-coverage'
                    elif percentage >= 60:
                        coverage_class = 'medium-coverage'
                    else:
                        coverage_class = 'low-coverage'
                    
                    prefix.append(
                        f'<tr><td>{rel_filename}</td>'
                        f'<td>{statements}</td>'
                        f'<td>{missing}</td>'
                        f'<td class="{coverage_class}">{percentage:.2f}%</td></tr>'
                    )
                    
            # Calculate total coverage
            if total_statements > 0:
                total_coverage = ((total_statements - total_missed) / total_statements) * 100
                if total_coverage >= 80:
                    coverage_class = 'high-coverage'
                elif total_coverage >= 60:
                    coverage_class = 'medium-coverage'
                else:
                    coverage_class = 'low-coverage'
                
                # Add total row
                prefix.append(
                    f'<tr style="font-weight: bold;"><td>TOTAL</td>'
                    f'<td>{total_statements}</td>'
                    f'<td>{total_missed}</td>'
                    f'<td class="{coverage_class}">{total_coverage:.2f}%</td></tr>'
                )
            
            prefix.append('</table></div>')
    except Exception as e:
        prefix.append(f'<div>Error generating coverage report: {str(e)}</div>')
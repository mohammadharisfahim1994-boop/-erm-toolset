"""
Enterprise Risk Management (ERM) Comprehensive Toolset
Tools for audit process automation and documentation
"""

import pandas as pd
import json
from datetime import datetime
from typing import List, Dict, Optional
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import re


class ProcessFlowGenerator:
    """Generate process flow documentation from field notes"""
    
    def __init__(self):
        self.process_steps = []
    
    def parse_field_notes(self, notes: str) -> List[Dict]:
        """
        Parse field notes into structured process steps
        Expected format: numbered steps or bullet points
        """
        lines = notes.strip().split('\n')
        steps = []
        
        step_num = 1
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Remove common prefixes
            line = re.sub(r'^[\d]+[\.\)]\s*', '', line)
            line = re.sub(r'^[-*•]\s*', '', line)
            
            if len(line) > 10:  # Meaningful step
                steps.append({
                    'step_number': step_num,
                    'description': line,
                    'actors': [],
                    'systems': [],
                    'documents': [],
                    'controls': []
                })
                step_num += 1
        
        self.process_steps = steps
        return steps
    
    def enhance_with_metadata(self, 
                             step_number: int,
                             actors: List[str] = None,
                             systems: List[str] = None,
                             documents: List[str] = None,
                             controls: List[str] = None):
        """Add metadata to specific process step"""
        if step_number <= len(self.process_steps):
            step = self.process_steps[step_number - 1]
            if actors:
                step['actors'] = actors
            if systems:
                step['systems'] = systems
            if documents:
                step['documents'] = documents
            if controls:
                step['controls'] = controls
    
    def export_to_excel(self, filename: str):
        """Export process flow to Excel"""
        df = pd.DataFrame(self.process_steps)
        df.to_excel(filename, index=False)
        print(f"✓ Process flow exported to {filename}")
    
    def export_to_word(self, filename: str, process_name: str):
        """Export process flow to formatted Word document"""
        doc = Document()
        
        # Title
        title = doc.add_heading(f'Process Flow: {process_name}', 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        doc.add_paragraph(f'Generated: {datetime.now().strftime("%Y-%m-%d")}')
        doc.add_paragraph()
        
        # Process steps
        for step in self.process_steps:
            # Step header
            heading = doc.add_heading(f'Step {step["step_number"]}', level=2)
            
            # Description
            doc.add_paragraph(step['description'])
            
            # Metadata
            if step['actors']:
                p = doc.add_paragraph()
                p.add_run('Actors: ').bold = True
                p.add_run(', '.join(step['actors']))
            
            if step['systems']:
                p = doc.add_paragraph()
                p.add_run('Systems: ').bold = True
                p.add_run(', '.join(step['systems']))
            
            if step['documents']:
                p = doc.add_paragraph()
                p.add_run('Documents: ').bold = True
                p.add_run(', '.join(step['documents']))
            
            if step['controls']:
                p = doc.add_paragraph()
                p.add_run('Controls: ').bold = True
                p.add_run(', '.join(step['controls']))
            
            doc.add_paragraph()
        
        doc.save(filename)
        print(f"✓ Process flow documentation saved to {filename}")


class GapAnalyzer:
    """Perform gap analysis from walkthrough observations"""
    
    def __init__(self):
        self.gaps = []
    
    def analyze_walkthrough(self,
                          documented_steps: List[str],
                          observed_steps: List[str],
                          policy_requirements: List[str] = None) -> List[Dict]:
        """
        Identify gaps between documented and observed processes
        
        Returns list of gaps with categorization
        """
        gaps = []
        
        # Missing steps (documented but not observed)
        for idx, doc_step in enumerate(documented_steps):
            if doc_step not in observed_steps:
                gaps.append({
                    'gap_id': f'GAP-{len(gaps)+1:03d}',
                    'gap_type': 'Missing Step',
                    'severity': 'High',
                    'documented': doc_step,
                    'observed': 'Step not performed',
                    'recommendation': f'Implement or enforce: {doc_step}'
                })
        
        # Extra steps (observed but not documented)
        for obs_step in observed_steps:
            if obs_step not in documented_steps:
                gaps.append({
                    'gap_id': f'GAP-{len(gaps)+1:03d}',
                    'gap_type': 'Undocumented Step',
                    'severity': 'Medium',
                    'documented': 'Not documented',
                    'observed': obs_step,
                    'recommendation': f'Document procedure: {obs_step}'
                })
        
        # Policy compliance gaps
        if policy_requirements:
            for policy in policy_requirements:
                if not any(policy.lower() in step.lower() for step in observed_steps):
                    gaps.append({
                        'gap_id': f'GAP-{len(gaps)+1:03d}',
                        'gap_type': 'Policy Non-Compliance',
                        'severity': 'High',
                        'documented': policy,
                        'observed': 'Requirement not met',
                        'recommendation': f'Ensure compliance with: {policy}'
                    })
        
        self.gaps = gaps
        return gaps
    
    def export_gap_report(self, filename: str):
        """Export gap analysis to Excel"""
        if not self.gaps:
            print("⚠ No gaps to export")
            return
        
        df = pd.DataFrame(self.gaps)
        df.to_excel(filename, index=False)
        print(f"✓ Gap analysis exported to {filename}")


class RiskAssessor:
    """Assess risks at process and function level"""
    
    def __init__(self):
        self.risk_matrix = {
            'likelihood': {
                'Rare': 1,
                'Unlikely': 2,
                'Possible': 3,
                'Likely': 4,
                'Almost Certain': 5
            },
            'impact': {
                'Insignificant': 1,
                'Minor': 2,
                'Moderate': 3,
                'Major': 4,
                'Catastrophic': 5
            }
        }
        self.risks = []
    
    def calculate_risk_score(self, likelihood: str, impact: str) -> tuple:
        """Calculate inherent risk score and rating"""
        l_score = self.risk_matrix['likelihood'].get(likelihood, 3)
        i_score = self.risk_matrix['impact'].get(impact, 3)
        risk_score = l_score * i_score
        
        # Determine rating
        if risk_score >= 15:
            rating = 'Critical'
        elif risk_score >= 10:
            rating = 'High'
        elif risk_score >= 5:
            rating = 'Medium'
        else:
            rating = 'Low'
        
        return risk_score, rating
    
    def assess_process_risks(self,
                            process_name: str,
                            process_steps: List[Dict],
                            risk_catalog: List[Dict] = None) -> List[Dict]:
        """
        Assess risks for each process step
        
        risk_catalog format: [{'risk_event': '', 'likelihood': '', 'impact': '', 'category': ''}]
        """
        if risk_catalog:
            for risk in risk_catalog:
                score, rating = self.calculate_risk_score(
                    risk.get('likelihood', 'Possible'),
                    risk.get('impact', 'Moderate')
                )
                
                self.risks.append({
                    'process': process_name,
                    'risk_id': f'RISK-{len(self.risks)+1:03d}',
                    'risk_event': risk.get('risk_event', ''),
                    'category': risk.get('category', 'Operational'),
                    'likelihood': risk.get('likelihood', 'Possible'),
                    'impact': risk.get('impact', 'Moderate'),
                    'inherent_risk_score': score,
                    'inherent_risk_rating': rating,
                    'existing_controls': risk.get('controls', []),
                    'residual_risk_rating': '',
                    'treatment': ''
                })
        
        return self.risks
    
    def export_risk_assessment(self, filename: str):
        """Export risk assessment to Excel"""
        if not self.risks:
            print("⚠ No risks to export")
            return
        
        df = pd.DataFrame(self.risks)
        df.to_excel(filename, index=False)
        print(f"✓ Risk assessment exported to {filename}")


class RCMGenerator:
    """Generate Risk and Control Matrix (RCM)"""
    
    def __init__(self):
        self.rcm_entries = []
    
    def generate_rcm(self,
                    process_name: str,
                    risks: List[Dict],
                    controls: List[Dict]) -> pd.DataFrame:
        """
        Generate RCM from risks and controls
        
        controls format: [{'control_id': '', 'description': '', 'type': 'preventive/detective', 
                          'frequency': '', 'owner': '', 'risk_addressed': []}]
        """
        rcm_data = []
        
        for risk in risks:
            risk_id = risk.get('risk_id', '')
            
            # Find controls that address this risk
            related_controls = [
                ctrl for ctrl in controls
                if risk_id in ctrl.get('risk_addressed', [])
            ]
            
            if related_controls:
                for ctrl in related_controls:
                    rcm_data.append({
                        'Process': process_name,
                        'Risk_ID': risk_id,
                        'Risk_Description': risk.get('risk_event', ''),
                        'Risk_Category': risk.get('category', ''),
                        'Inherent_Risk': risk.get('inherent_risk_rating', ''),
                        'Control_ID': ctrl.get('control_id', ''),
                        'Control_Description': ctrl.get('description', ''),
                        'Control_Type': ctrl.get('type', ''),
                        'Control_Frequency': ctrl.get('frequency', ''),
                        'Control_Owner': ctrl.get('owner', ''),
                        'Design_Effectiveness': '',
                        'Operating_Effectiveness': '',
                        'Residual_Risk': ''
                    })
            else:
                # Risk without control
                rcm_data.append({
                    'Process': process_name,
                    'Risk_ID': risk_id,
                    'Risk_Description': risk.get('risk_event', ''),
                    'Risk_Category': risk.get('category', ''),
                    'Inherent_Risk': risk.get('inherent_risk_rating', ''),
                    'Control_ID': 'No Control',
                    'Control_Description': 'Control Gap Identified',
                    'Control_Type': 'N/A',
                    'Control_Frequency': 'N/A',
                    'Control_Owner': 'TBD',
                    'Design_Effectiveness': 'N/A',
                    'Operating_Effectiveness': 'N/A',
                    'Residual_Risk': risk.get('inherent_risk_rating', '')
                })
        
        self.rcm_entries = rcm_data
        return pd.DataFrame(rcm_data)
    
    def export_rcm(self, filename: str):
        """Export RCM to Excel with formatting"""
        if not self.rcm_entries:
            print("⚠ No RCM entries to export")
            return
        
        df = pd.DataFrame(self.rcm_entries)
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='RCM', index=False)
            
            # Get workbook and worksheet
            workbook = writer.book
            worksheet = writer.sheets['RCM']
            
            # Auto-adjust column widths
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = min(max_length + 2, 50)
                worksheet.column_dimensions[column_letter].width = adjusted_width
        
        print(f"✓ RCM exported to {filename}")


class POLGenerator:
    """Generate Potential Observations Library (POL)"""
    
    def __init__(self):
        self.observations = []
    
    def generate_pol_from_gaps(self, gaps: List[Dict], rcm_data: pd.DataFrame = None):
        """Generate potential observations from gap analysis and RCM"""
        
        for gap in gaps:
            obs = {
                'observation_id': f'OBS-{len(self.observations)+1:03d}',
                'source': 'Gap Analysis',
                'title': f'{gap["gap_type"]}: {gap["documented"][:50]}...',
                'condition': gap['observed'],
                'criteria': gap['documented'],
                'cause': 'TBD - To be determined during fieldwork',
                'effect': 'Potential process inefficiency or control weakness',
                'risk_rating': gap['severity'],
                'recommendation': gap['recommendation'],
                'status': 'Potential - Requires Validation'
            }
            self.observations.append(obs)
        
        # Add observations from control gaps in RCM
        if rcm_data is not None:
            control_gaps = rcm_data[rcm_data['Control_ID'] == 'No Control']
            for _, row in control_gaps.iterrows():
                obs = {
                    'observation_id': f'OBS-{len(self.observations)+1:03d}',
                    'source': 'RCM Analysis',
                    'title': f'Control Gap: {row["Risk_Description"][:50]}...',
                    'condition': 'No control exists to mitigate identified risk',
                    'criteria': 'Risk should be mitigated by appropriate controls',
                    'cause': 'Control design gap',
                    'effect': f'Unmitigated {row["Inherent_Risk"]} risk',
                    'risk_rating': row['Inherent_Risk'],
                    'recommendation': f'Implement control to address: {row["Risk_Description"]}',
                    'status': 'Potential - Requires Validation'
                }
                self.observations.append(obs)
        
        return self.observations
    
    def export_pol(self, filename: str):
        """Export POL to Excel"""
        if not self.observations:
            print("⚠ No observations to export")
            return
        
        df = pd.DataFrame(self.observations)
        df.to_excel(filename, index=False)
        print(f"✓ Potential Observations Library exported to {filename}")


class AuditProgramFormulator:
    """Formulate audit program from process and risk information"""
    
    def __init__(self):
        self.audit_procedures = []
    
    def generate_procedures(self,
                          process_name: str,
                          rcm_data: pd.DataFrame,
                          focus_areas: List[str] = None):
        """Generate audit procedures based on RCM"""
        
        procedures = []
        proc_num = 1
        
        # Group by control
        if not rcm_data.empty:
            for _, row in rcm_data.iterrows():
                # Design effectiveness test
                procedures.append({
                    'procedure_id': f'AP-{proc_num:03d}',
                    'objective': 'Design Effectiveness',
                    'procedure': f'Review and evaluate the design of {row["Control_ID"]}: {row["Control_Description"]}',
                    'control_tested': row['Control_ID'],
                    'risk_addressed': row['Risk_ID'],
                    'test_type': 'Inquiry and Inspection',
                    'sample_size': 'N/A',
                    'expected_evidence': 'Policy documentation, procedure manuals'
                })
                proc_num += 1
                
                # Operating effectiveness test
                if row['Control_Type'] != 'N/A':
                    procedures.append({
                        'procedure_id': f'AP-{proc_num:03d}',
                        'objective': 'Operating Effectiveness',
                        'procedure': f'Test operating effectiveness of {row["Control_ID"]} by examining sample transactions',
                        'control_tested': row['Control_ID'],
                        'risk_addressed': row['Risk_ID'],
                        'test_type': 'Sample Testing',
                        'sample_size': self._determine_sample_size(row.get('Inherent_Risk', 'Medium')),
                        'expected_evidence': 'Transaction logs, approval records, system reports'
                    })
                    proc_num += 1
        
        self.audit_procedures = procedures
        return procedures
    
    def _determine_sample_size(self, risk_rating: str) -> str:
        """Determine sample size based on risk"""
        risk_samples = {
            'Critical': '30-40',
            'High': '25-30',
            'Medium': '15-25',
            'Low': '10-15'
        }
        return risk_samples.get(risk_rating, '20-25')
    
    def export_audit_program(self, filename: str, process_name: str):
        """Export audit program to Excel"""
        if not self.audit_procedures:
            print("⚠ No procedures to export")
            return
        
        df = pd.DataFrame(self.audit_procedures)
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Audit Program', index=False)
            
            # Add title sheet
            title_df = pd.DataFrame({
                'Audit Program': [process_name],
                'Date': [datetime.now().strftime('%Y-%m-%d')],
                'Total Procedures': [len(self.audit_procedures)]
            })
            title_df.to_excel(writer, sheet_name='Cover', index=False)
        
        print(f"✓ Audit program exported to {filename}")


class AuditLogGenerator:
    """Generate consolidated audit log for report population"""
    
    def __init__(self):
        self.log_entries = []
    
    def consolidate_findings(self,
                           validated_observations: List[Dict],
                           testing_results: pd.DataFrame = None) -> pd.DataFrame:
        """
        Consolidate validated observations into audit log
        
        validated_observations: List of dicts with observation details
        testing_results: DataFrame with control testing results
        """
        
        log_data = []
        
        for obs in validated_observations:
            # Determine if this becomes a finding
            if obs.get('status') == 'Confirmed':
                log_entry = {
                    'Finding_ID': obs.get('observation_id', '').replace('OBS', 'F'),
                    'Title': obs.get('title', ''),
                    'Process_Area': obs.get('process_area', ''),
                    'Observation': obs.get('condition', ''),
                    'Criteria': obs.get('criteria', ''),
                    'Cause': obs.get('cause', ''),
                    'Effect_Impact': obs.get('effect', ''),
                    'Risk_Rating': obs.get('risk_rating', ''),
                    'Recommendation': obs.get('recommendation', ''),
                    'Management_Response': obs.get('management_response', 'Pending'),
                    'Target_Completion_Date': obs.get('target_date', ''),
                    'Responsible_Party': obs.get('owner', ''),
                    'Status': 'Open',
                    'Evidence_Reference': obs.get('evidence', '')
                }
                log_data.append(log_entry)
        
        # Add testing exceptions if provided
        if testing_results is not None and not testing_results.empty:
            exception_rows = testing_results[testing_results['Test_Result'] == 'Exception']
            for _, row in exception_rows.iterrows():
                log_entry = {
                    'Finding_ID': f'F-{len(log_data)+1:03d}',
                    'Title': f'Control Exception: {row.get("Control_ID", "")}',
                    'Process_Area': row.get('Process', ''),
                    'Observation': row.get('Exception_Details', ''),
                    'Criteria': row.get('Control_Description', ''),
                    'Cause': 'Control not operating effectively',
                    'Effect_Impact': 'Risk exposure',
                    'Risk_Rating': row.get('Risk_Rating', 'Medium'),
                    'Recommendation': 'Strengthen control or implement compensating control',
                    'Management_Response': 'Pending',
                    'Target_Completion_Date': '',
                    'Responsible_Party': row.get('Control_Owner', ''),
                    'Status': 'Open',
                    'Evidence_Reference': row.get('Test_Reference', '')
                }
                log_data.append(log_entry)
        
        self.log_entries = log_data
        return pd.DataFrame(log_data)
    
    def export_audit_log(self, filename: str):
        """Export audit log to Excel (ready for report auto-population)"""
        if not self.log_entries:
            print("⚠ No log entries to export")
            return
        
        df = pd.DataFrame(self.log_entries)
        df.to_excel(filename, index=False)
        print(f"✓ Audit log exported to {filename}")
        print(f"  This file can now be used with the Audit Report Generator")


def main():
    """Demonstration of ERM Toolset"""
    
    print("="*70)
    print("ERM TOOLSET DEMONSTRATION")
    print("="*70)
    
    # 1. Process Flow Generation
    print("\n1. PROCESS FLOW GENERATION")
    print("-"*70)
    field_notes = """
    1. Requestor creates purchase requisition in system
    2. Manager reviews and approves requisition
    3. Procurement team creates purchase order
    4. Vendor delivers goods with packing slip
    5. Warehouse receives goods and creates GRN
    6. AP team receives invoice
    7. System performs 3-way match
    8. Payment is processed
    """
    
    flow_gen = ProcessFlowGenerator()
    steps = flow_gen.parse_field_notes(field_notes)
    flow_gen.enhance_with_metadata(1, actors=['Requestor'], systems=['ERP System'])
    flow_gen.export_to_excel('process_flow.xlsx')
    flow_gen.export_to_word('process_flow.docx', 'Procure-to-Pay Process')
    
    # 2. Gap Analysis
    print("\n2. GAP ANALYSIS")
    print("-"*70)
    documented = ['Manager approval required', 'Three-way match mandatory', 'Segregation of duties']
    observed = ['Manager approval obtained', 'Segregation of duties implemented']
    
    gap_analyzer = GapAnalyzer()
    gaps = gap_analyzer.analyze_walkthrough(documented, observed)
    gap_analyzer.export_gap_report('gap_analysis.xlsx')
    print(f"Found {len(gaps)} gaps")
    
    # 3. Risk Assessment
    print("\n3. RISK ASSESSMENT")
    print("-"*70)
    risk_catalog = [
        {'risk_event': 'Unauthorized purchases', 'likelihood': 'Possible', 'impact': 'Major', 'category': 'Operational'},
        {'risk_event': 'Duplicate payments', 'likelihood': 'Unlikely', 'impact': 'Moderate', 'category': 'Financial'}
    ]
    
    risk_assessor = RiskAssessor()
    risks = risk_assessor.assess_process_risks('Procure-to-Pay', steps, risk_catalog)
    risk_assessor.export_risk_assessment('risk_assessment.xlsx')
    
    # 4. RCM Generation
    print("\n4. RCM GENERATION")
    print("-"*70)
    controls = [
        {'control_id': 'P2P-001', 'description': 'System approval workflow', 'type': 'preventive',
         'frequency': 'Continuous', 'owner': 'IT', 'risk_addressed': ['RISK-001']},
        {'control_id': 'P2P-002', 'description': '3-way match', 'type': 'detective',
         'frequency': 'Per transaction', 'owner': 'AP Manager', 'risk_addressed': ['RISK-002']}
    ]
    
    rcm_gen = RCMGenerator()
    rcm_df = rcm_gen.generate_rcm('Procure-to-Pay', risks, controls)
    rcm_gen.export_rcm('rcm.xlsx')
    
    # 5. POL Generation
    print("\n5. POTENTIAL OBSERVATIONS LIBRARY")
    print("-"*70)
    pol_gen = POLGenerator()
    pol_gen.generate_pol_from_gaps(gaps, rcm_df)
    pol_gen.export_pol('potential_observations.xlsx')
    
    # 6. Audit Program
    print("\n6. AUDIT PROGRAM FORMULATION")
    print("-"*70)
    ap_gen = AuditProgramFormulator()
    ap_gen.generate_procedures('Procure-to-Pay', rcm_df)
    ap_gen.export_audit_program('audit_program.xlsx', 'Procure-to-Pay Audit')
    
    # 7. Audit Log
    print("\n7. AUDIT LOG GENERATION")
    print("-"*70)
    validated_obs = [
        {
            'observation_id': 'OBS-001',
            'status': 'Confirmed',
            'title': 'Missing three-way match',
            'condition': '3-way match not consistently performed',
            'criteria': 'Policy requires 3-way match',
            'cause': 'System configuration allows bypass',
            'effect': 'Risk of duplicate payments',
            'risk_rating': 'High',
            'recommendation': 'Enforce system controls',
            'process_area': 'Procure-to-Pay'
        }
    ]
    
    log_gen = AuditLogGenerator()
    log_df = log_gen.consolidate_findings(validated_obs)
    log_gen.export_audit_log('findings_log.xlsx')
    
    print("\n" + "="*70)
    print("✓ ALL TOOLS DEMONSTRATED SUCCESSFULLY")
    print("="*70)
    print("\nGenerated files:")
    print("  - process_flow.xlsx & .docx")
    print("  - gap_analysis.xlsx")
    print("  - risk_assessment.xlsx")
    print("  - rcm.xlsx")
    print("  - potential_observations.xlsx")
    print("  - audit_program.xlsx")
    print("  - findings_log.xlsx (ready for report generator)")


if __name__ == "__main__":
    main()

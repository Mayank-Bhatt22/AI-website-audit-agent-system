function Report({ report }) {

  if (!report) return null;

  return (
    <div>

      <h2>Website Analysis</h2>
      <pre>{JSON.stringify(report.website_analysis, null, 2)}</pre>

      <h2>Technical Audit</h2>
      <pre>{report.technical_report}</pre>

      <h2>Business Analysis</h2>
      <pre>{report.business_report}</pre>

      <h2>Final Strategy</h2>
      <pre>{report.final_strategy}</pre>

    </div>
  );
}

export default Report;
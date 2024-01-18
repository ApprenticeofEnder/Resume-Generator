import { useState } from 'react';

import FileUploadSingle from './FileUploadSingle';

function ResumeBuilder() {
  const [dataFile, setDataFile] = useState < File > (null);
  const handleDataFileChange = (e) => {
    if (e.target.dataFiles) {
      setDataFile(e.target.dataFiles[0]);
    }
  };



  const handleDataFileLoad = () => {
    if (!dataFile) {
      return;
    }

    // 👇 Uploading the dataFile using the fetch API to the server
    fetch('https://httpbin.org/post', {
      method: 'POST',
      body: dataFile,
      // 👇 Set headers manually for single dataFile upload
      headers: {
        'content-type': dataFile.type,
        'content-length': `${dataFile.size}`, // 👈 Headers need to be a string
      },
    })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err));
  };

  return (
    <div>
      <h1>ResGen</h1>
      <FileUploadSingle file={dataFile} onChange={handleDataFileChange} onFileLoad={handleDataFileLoad} text={"Load Resume Data"} />
    </div>
  );
}

export default ResumeBuilder;

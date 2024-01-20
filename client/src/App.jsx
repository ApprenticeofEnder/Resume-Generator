import { useState } from 'react';
import YAML from 'yaml';
import './App.css';
import FileUploadSingle from './components/FileUploadSingle';

function App() {
    const [dataFile, setDataFile] = useState({});
    const [resumeData, setResumeData] = useState({});

    const handleDataFileChange = (e) => {
        if (e.target.files) {
            setDataFile(e.target.files[0]);
        }
    };

    const handleDataFileLoad = async () => {
        if (!dataFile) {
            return;
        }

        let data = await dataFile.text();

        let loaded_resume_data = YAML.parse(data);
        setResumeData(loaded_resume_data);
        console.table(resumeData);
    };

    return (
        <>
            <h1>ResGen</h1>
            <FileUploadSingle
                file={dataFile}
                onChange={handleDataFileChange}
                onFileLoad={handleDataFileLoad}
                text={'Load Resume Data'}
            />
        </>
    );
}

export default App;

import PropTypes from "prop-types";

function FileUploadSingle({ file, onChange, onFileLoad, text }) {
  return (
    <div>
      <input type="file" onChange={onChange} />

      <div>{file && `${file.name} - ${file.type}`}</div>

      <button onClick={onFileLoad}>{text}</button>
    </div>
  );
}

FileUploadSingle.propTypes = {
  file: PropTypes.object,
  onChange: PropTypes.func,
  onFileLoad: PropTypes.func,
  text: PropTypes.string,
};

export default FileUploadSingle;

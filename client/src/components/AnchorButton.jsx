import "./AnchorButton.css";

//returns a html anchor tag that looks like a button
function AnchorButton({ text, reference }) {
  return <a href={reference}>{text}</a>;
}

export default AnchorButton;

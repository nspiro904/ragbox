import "./AnchorButton.scss"

export default function AnchorButton(props) {

  return (
    <a href={props.route} class="btn">{props.text}</a>
  );
}
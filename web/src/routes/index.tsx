import { Title } from "@solidjs/meta";
import AnchorButton from "~/components/AnchorButton/AnchorButton";
export default function Home() {

  
  return (
    <main>
      <Title>Rag in a Box</Title>
      <h1>Rag in a Box</h1>
      <AnchorButton text="hello" route="./test" />
      <AnchorButton text="Create Model" route="./model/new"/>
    </main>
  );
}
import Image from "next/image";
import image1 from "./assets/image1.png";
import image2 from "./assets/image2.jpg";
import image3 from "./assets/image3.jpg";
import image4 from "./assets/image4.jpg";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "./components/accordion";
import Header from "./components/Header";
import Step2 from "./components/step2";
import Step3 from "./components/step3";
import Step4 from "./components/step4";

export type Data = {
  raw_imgs: any;
  img_ids: any;
  progression: any;
  step_index: any;
  step_id: any;
  user_id: any;
  time_interval: any;
  prev_step_id: any;
  next_step_id: any;
}

export default function Home() {
  return (
    <div className="flex flex-col justify-start items-start bg-black1 h-dvh p-12 w-full overflow-x-auto space-y-12">
      <nav className="w-full flex justify-between items-center px-8 bg-black1 text-gray-100">
        <div className="text-xl font-bold hover:text-sage2 duration-300 cursor-pointer">Home</div>
        <div className="flex space-x-8">
          <div className="text-xl font-bold hover:text-sage2 duration-300 cursor-pointer">Guides</div>
          <div className="text-xl font-bold hover:text-sage2 duration-300 cursor-pointer">Create</div>
        </div>
      </nav>
      <h1 className="text-5xl font-bold uppercase text-gray-100 pl-7 pb-8">LEGO AT-AT Walker Construction Guide</h1>
      <div className="flex flex-row justify-start items-center w-full space-x-48">
      <Accordion className="min-w-lg max-w-xl border-2 border-black2 rounded-lg" type="single" collapsible>
        <AccordionItem value="item-1" className="group data-[state=open]:bg-black1 hover:bg-black2 rounded-lg duration-300">
          <AccordionTrigger className="duration-300">
            <b>Step 1</b> <b className="pt-1 pb-2 font-normal text-center">{data[0].progression}</b>
          </AccordionTrigger>
          <AccordionContent className="max-h-[65dvh] overflow-y-auto pr-4">
          <div className="flex flex-col space-y-4">
            <Header title="Tools: " value="Lego Box, Manual" size="small" colorClassName="accent1" />
            <h3 className="text-2xl font-semibold text-center text-gray-100 pt-4">Action Items</h3>
            <div className="border-sage2 border-[0.75px] rounded-lg" /> 
            <div className="flex py-4">
              <div className="w-1/3 rounded-lg">
                <Image className="rounded-lg" src={image1} alt="Description 1" width={100} height={100} layout="responsive" />
              </div>
              <div className="w-2/3 pl-4 flex items-center">
                <ul className="list-disc pl-5 space-y-1">
                  <li className="text-md text-gray-100">Prepare a big, flat area as your workspace.</li>
                  <li className="text-md text-gray-100">Take the contents out of the <span className="text-sage2 font-bold">Lego Box.</span></li>
                  <li className="text-md text-gray-100">Read the <span className="text-sage2 font-bold">Manual</span> and ensure all pieces are present.</li>
                </ul>
              </div>
            </div>
          </div>
          </AccordionContent>
        </AccordionItem>
      </Accordion>
      <div className="flex flex-col space-y-8 min-w-sm">
        <Step2 value="a" index="1" image={image2} tools="Scissors, Manual" desc1="Use the Scissors to cut open bags 1-3." desc2="Read the Manual and begin with step 1-5."/>
        <Step2 value="b" index="2" image={image3} tools="Yellow bricks, Blue bricks, Red bricks, Manual" desc1="Use the blue and yellow bricks and the Manual to complete steps 6-11." desc2="Read the Manual and use the red bricks to begin with steps 12 and 13."/>
        <Step2 value="c" index="3" image={image4} tools="Manual" desc1="Take special note of the following pieces." desc2="Follow the Manual carefully for steps 14 and 15."/>
      </div>
      <Step3/>
      <Step4/>
    </div>
  </div>
  );
}

export const data: Data[] = [
  {
      raw_imgs: [],
      img_ids: [160],
      progression: "All LEGO pieces are laid out in organized packets for assembly.",
      step_index: 1,
      step_id: "step_001",
      user_id: "user_who_contributed",
      time_interval: "2024-10-26 21:05:11.990211 to 2024-10-26 21:05:16.130469",
      prev_step_id: "",
      next_step_id: "step_002"
  },
  {
      raw_imgs: [],
      img_ids: [456, 621, 408, 113],
      progression: "Preparing lego pieces to begin building.",
      step_index: 2,
      step_id: "step_002",
      user_id: "user_who_contributed",
      time_interval: "2024-10-26 21:05:16.130469 to 2024-10-26 21:05:23.416128",
      prev_step_id: "step_001",
      next_step_id: "step_003"
  },
  {
      raw_imgs: [],
      img_ids: [160],
      progression: "Attaching various colored bricks to form a structured framework.",
      step_index: 1,
      step_id: "step_001",
      user_id: "user_who_contributed",
      time_interval: "2024-10-26 21:05:11.990211 to 2024-10-26 21:05:16.130469",
      prev_step_id: "",
      next_step_id: "step_002"
  },
  {
    raw_imgs: [],
    img_ids: [160],
    progression: "Attatching special pieces.",
    step_index: 1,
    step_id: "step_001",
    user_id: "user_who_contributed",
    time_interval: "2024-10-26 21:05:11.990211 to 2024-10-26 21:05:16.130469",
    prev_step_id: "",
    next_step_id: "step_002"
},
{
    raw_imgs: [],
    img_ids: [621, 408],
    progression: "Attaching yellow and blue LEGO bricks to the existing structured framework.",
    step_index: 3,
    step_id: "step_003",
    user_id: "user_who_contributed",
    time_interval: "2024-10-26 21:05:18.431565 to 2024-10-26 21:05:20.774452",
    prev_step_id: "step_002",
    next_step_id: "step_004"
},
{
    raw_imgs: [],
    img_ids: [113],
    progression: "Attaching blue LEGO bricks to the existing structured framework.",
    step_index: 4,
    step_id: "step_004",
    user_id: "user_who_contributed",
    time_interval: "2024-10-26 21:05:20.774452 to 2024-10-26 21:05:23.416128",
    prev_step_id: "step_003",
    next_step_id: null
},
  {
      raw_imgs: [],
      img_ids: [160],
      progression: "All LEGO pieces are laid out in organized packets for assembly.",
      step_index: 1,
      step_id: "step_001",
      user_id: "user_who_contributed",
      time_interval: "2024-10-26 21:05:11.990211 to 2024-10-26 21:05:16.130469",
      prev_step_id: null,
      next_step_id: "step_002"
  },
  {
      raw_imgs: [],
      img_ids: [456],
      progression: "Assembling LEGO pieces together to form a structured framework.",
      step_index: 2,
      step_id: "step_002",
      user_id: "user_who_contributed",
      time_interval: "2024-10-26 21:05:16.130469 to 2024-10-26 21:05:18.431565",
      prev_step_id: "step_001",
      next_step_id: "step_003"
  },
  {
      raw_imgs: [],
      img_ids: [621, 408],
      progression: "Attaching yellow and blue LEGO bricks to the existing structured framework.",
      step_index: 3,
      step_id: "step_003",
      user_id: "user_who_contributed",
      time_interval: "2024-10-26 21:05:18.431565 to 2024-10-26 21:05:20.774452",
      prev_step_id: "step_002",
      next_step_id: "step_004"
  },
  {
      raw_imgs: [],
      img_ids: [113],
      progression: "Attaching blue LEGO bricks to the existing structured framework.",
      step_index: 4,
      step_id: "step_004",
      user_id: "user_who_contributed",
      time_interval: "2024-10-26 21:05:20.774452 to 2024-10-26 21:05:23.416128",
      prev_step_id: "step_003",
      next_step_id: null
  }
]

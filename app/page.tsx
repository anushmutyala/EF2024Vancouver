import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "./components/accordion";

export default function Home() {
  return (
    <div className="flex flex-col justify-center">
      <div className="pt-12 pl-12">
          <Accordion className="max-w-lg border-1 border-gray-300 rounded-lg bg-white shadow-[0_2px_10px] shadow-black/5" type="single" collapsible>
            <AccordionItem value="item-1" className="group data-[state=open]:bg-accent2 hover:bg-accent2 rounded-lg duration-300">
              <AccordionTrigger className="group-data-[state=open]:text-gray-100 group-hover:text-gray-100 duration-200">
                <b>Step 1: Short description of the step</b>
              </AccordionTrigger>
              <AccordionContent>
                Our matching algorithm uses advanced AI to pair students and
                tutors based on their profiles, learning styles, and teaching
                methods to ensure the best possible match for success.
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        </div>
    </div>
  );
}

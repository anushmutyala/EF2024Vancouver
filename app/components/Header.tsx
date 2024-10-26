// 'use client';

type HeaderProps = {
  title: any;
  value: any;
  subvalue?: any;
  size: 'small' | 'medium' | 'large';
  colorClassName?: any;
  fixedWidth?: boolean;
}

export default function Header({title, value, size = 'small', colorClassName, subvalue, fixedWidth}: HeaderProps) {
  switch(size) {
    case 'small': {
      return (
        <div className="flex flex-row mt-2 py-2 border-2 border-sage2 rounded-xl">
          <span className="text-md pl-4 text-gray-100 font-bold select-none">
            {title}
          </span>
            <span className="text-md pr-4 text-gray-100 font-semibold pl-2">
            {value}
          </span>
        </div>
      );
    }
    case 'medium': {
      return (
        <div className="flex flex-col justify-between py-4 min-h-[200px] min-w-[200px] max-w-[250px] 2xl:max-w-[275px] group bg-accent3 border-2 border-accent3 rounded-lg hover:scale-105 hover:shadow-md duration-300">
          <h3 className="flex px-4 text-gray-100 text-align-left font-semibold text-lg 2xl:text-xl items-center justify-center select-none">
            {title}
          </h3>
          <div className="flex flex-col px-4 select-none">
            <span className="text-gray-100 text-align-left font-semibold text-sm 2xl:text-md -mt-1">{subvalue}</span>
          </div>
        </div>
      );
    }
    case 'large': {
      return (
        <div className={`flex flex-col pt-2 pb-1.5 px-4 ${fixedWidth ? 'w-[300px]': 'w-fit'} h-fit border-2 border-${colorClassName} rounded-lg hover:shadow-md duration-500 group bg-${colorClassName} items-center justify-center`}>
          <h3 className={`text-${colorClassName} font-bold ${fixedWidth ? 'text-3xl': 'text-4xl'} text-center flex-grow flex items-center justify-center select-none text-gray-100`}>
            {title}
          </h3>
        </div>
      );      
    }
  }
};
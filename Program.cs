using System;
using System.IO;

namespace gitkab
{
    class Program
    {
        static int Main(string[] args)
        {
            FileInfo ConfigFile = new FileInfo("config.cfg");

            if(args == null)
            {
                Console.WriteLine("No arguments found!");
                return 0;
            }
            else if (Array.IndexOf(args, "config") > -1)
            {
                if (!ConfigFile.Exists)
                {
                    FileStream Stream = ConfigFile.Create();
                    Stream.Close();
                }
                
                FileStream Writer = ConfigFile.OpenWrite();
                Console.WriteLine("API-Key:");
                string Key = Console.ReadLine();
                Console.WriteLine("Default Username:");
                string Username = Console.ReadLine();
                Console.WriteLine("Default Email:");
                string Email = Console.ReadLine();
                Console.WriteLine("Use GPG-Key? (y/n)");
                if (Console.ReadKey().Key == ConsoleKey.Y)
                {
                    Console.WriteLine("Enter GPG-Key:");
                    string GPGKey = Console.ReadLine();
                    Console.WriteLine("Done!");
                    // save & close
                    // get structure
                    return 1;
                }
                else if (Console.ReadKey().Key == ConsoleKey.N)
                {
                    Console.WriteLine("Done!");
                    // save & close
                    // get structure
                    return 1;
                }
                else
                {
                    Console.WriteLine("Invalid key -- assuming no");
                    // save & close
                    // get structure
                    return 1;
                }
            }
            else
            {
                return 0;
            }
        }
    }
}

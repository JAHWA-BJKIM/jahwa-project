##############################################################################
#                          [ Python Library ]                                                
#                                                                                
# Institution           : KAIST - SEED Lab         
# Created by            : Dalta Imam Maulana                                         
#                                                                                
# Project Name          : Jahwa I2C Sensor                                     
#                                                                                
# Create Date           : 05/16/2023
# File Name             : server.py                                           
#                                                                                
# Target Device         : PC                                                     
# Tool Version          : Python >= 3.6                                          
#       
##############################################################################

##############################################################################
#                              Import Libraries                              #
##############################################################################
# Python library
import re
import csv
import random
import asyncio

# User-defined library
from library.packet import *

##############################################################################
#                 Define Function to Handle Client Connection                #
##############################################################################
async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    # Keep listening to client until client send "quit" packet
    while True:
        # Wait for client to send data
        data = await reader.read(1024)

        # Get packet header
        transaction_id = data[0:2]
        protocol_id = data[2:4]
        length = data[4:6]
        unit_id = data[6:7]

        # Follow up operation based on packet type
        ######################################################################
        #                              Write I2C                             #
        ######################################################################
        if unit_id == unit_id_dict['write_i2c']:
            # Print status
            print("Received write I2C packet from client")

            # Decode packet
            packet = decode_packet(data)

            # Print decoded packet
            for key, value in packet.items():
                print(key, ":", value)
            print()

            # Send back data to the client
            writer.write(data)
            await writer.drain()

        ######################################################################
        #                              Read I2C                              #
        ######################################################################
        elif unit_id == unit_id_dict['read_i2c']:
            # Print status
            print("Received read I2C packet from client")

            # Decode packet
            packet = decode_packet(data)

            # Print decoded packet
            for key, value in packet.items():
                print(key, ":", value)
            print()

            # Create dummy response for client
            packet = encode_packet(
                'read_i2c',
                transaction_id=packet['transaction_id'],
                protocol_id=packet['protocol_id'],
                length=packet['length'],
                unit_id=packet['unit_id'],
                data_buf=packet['data_buf']
            )

            # Send back data to the client
            writer.write(packet)
            await writer.drain()

        ######################################################################
        #                           Pattern Loading                          #
        ######################################################################
        elif unit_id == unit_id_dict['pattern_loading']:
            # Print status
            print("Received pattern loading packet from client")

            # Decode data tp get write buffer size
            write_packet_size = int.from_bytes(data[20:24], byteorder='little')
            block_count = int.from_bytes(data[28:32], byteorder='little')
            measure_count = int.from_bytes(data[32:36], byteorder='little')
            write_buffer_size = write_packet_size * block_count * measure_count

            # Decode packet
            packet = decode_packet(data, write_buffer_size=write_buffer_size)

            # Print decoded packet
            for key, value in packet.items():
                print(key, ":", value)
            print()

            # Send back data to the client
            writer.write(data)
            await writer.drain()

        ######################################################################
        #                             Pattern Run                            #
        ######################################################################
        elif unit_id == unit_id_dict['pattern_run']:
            # Print status
            print("Received pattern run packet from client")

            # Decode packet
            packet = decode_packet(data)

            # Print decoded packet
            for key, value in packet.items():
                print(key, ":", value)
            print()

            # Send back data to the client
            writer.write(data)
            await writer.drain()

        ######################################################################
        #                          Pattern Get Data                          #
        ######################################################################
        elif unit_id == unit_id_dict['pattern_get_data']:
            # Print status
            print("Received pattern get data packet from client")

            # Decode packet
            packet = decode_packet(data)

            # Print decoded packet
            for key, value in packet.items():
                print(key, ":", value)
            print()

            # Create dummy response for client
            packet = encode_packet(
                'pattern_get_data',
                transaction_id=packet['transaction_id'],
                protocol_id=packet['protocol_id'],
                length=packet['length'],
                unit_id=packet['unit_id'],
                read_buffer_size=packet['read_buffer_size'],
                num_of_ldo_ch0_current=packet['num_of_ldo_ch0_current'],
                num_of_ldo_ch0_voltage=packet['num_of_ldo_ch0_voltage'],
                num_of_ldo_ch1_current=packet['num_of_ldo_ch1_current'],
                num_of_ldo_ch1_voltage=packet['num_of_ldo_ch1_voltage'],
                read_buffer=[str(i) for i in range(packet['read_buffer_size'])],
                ldo_ch0_current=[random.random() for i in range(packet['num_of_ldo_ch0_current'])],
                ldo_ch0_voltage=[random.random() for i in range(packet['num_of_ldo_ch0_voltage'])],
                ldo_ch1_current=[random.random() for i in range(packet['num_of_ldo_ch1_current'])],
                ldo_ch1_voltage=[random.random() for i in range(packet['num_of_ldo_ch1_voltage'])],
            )

            # Send back data to the client
            writer.write(packet)
            await writer.drain()

        ######################################################################
        #                           LDO Voltage Set                          #
        ######################################################################
        elif unit_id == unit_id_dict['ldo_voltage_set']:
            # Print status
            print("Received LDO voltage set packet from client")

            # Decode packet
            packet = decode_packet(data)

            # Print decoded packet
            for key, value in packet.items():
                print(key, ":", value)
            print()

            # Send back data to the client
            writer.write(data)
            await writer.drain()

        ##########################################################################
        #   Power Control, Burst Mode, Burst Write Delay, and Burst Read Delay   #
        ##########################################################################
        elif (unit_id == unit_id_dict['power_control']) or (unit_id == unit_id_dict['burst_mode']) or \
         (unit_id == unit_id_dict['burst_write_delay']) or (unit_id == unit_id_dict['burst_read_delay']):
            # Get command
            command = int.from_bytes(data[8:12], byteorder='little')
            
            # Print status based on command
            if command == 1:
                print("Received power control packet from client")
            elif command == 11:
                print("Received burst mode packet from client")
            elif command == 12:
                print("Received burst write delay packet from client")
            elif command == 13:
                print("Received burst read delay packet from client")
            else:
                print("Unknown command")

            # Decode packet
            packet = decode_packet(data)

            # Print decoded packet
            for key, value in packet.items():
                print(key, ":", value)
            print()

            # Send back data to the client
            writer.write(data)
            await writer.drain()

        ######################################################################
        #                           Burst Get Data                           #
        ######################################################################
        elif unit_id == unit_id_dict['burst_get_data']:
            # Print status
            print("Received burst get data packet from client")

            # Decode packet
            packet = decode_packet(data)

            # Print decoded packet
            for key, value in packet.items():
                print(key, ":", value)
            print()

            # Calculate read buffer size
            read_buffer_size = packet['read_packet_size']*packet['read_count']

            # Create dummy response for client
            packet = encode_packet(
                'burst_get_data',
                transaction_id=packet['transaction_id'],
                protocol_id=packet['protocol_id'],
                length=packet['length'],
                unit_id=packet['unit_id'],
                read_buffer_size=read_buffer_size,
                read_buffer=[str(i) for i in range(read_buffer_size)],
            )

            # Send back data to the client
            writer.write(packet)
            await writer.drain()

        ######################################################################
        #                                Quit                                #
        ######################################################################
        elif unit_id == unit_id_dict['quit']:
            # Print status
            print("Received quit packet from client")

            # Send back data to the client
            writer.write(data)
            await writer.drain()

            # Close connection
            break

        else:
            # Print status
            print("Received unknown packet from client")

            # Send back data to the client
            writer.write(data)
            await writer.drain()

    # Close connection
    print("Close the connection to the client")
    writer.close()
    await writer.wait_closed()

##############################################################################
#                              Define TCP Server                             #
##############################################################################
async def run_server(server_addr, server_port) -> None:
    server = await asyncio.start_server(handle_echo, server_addr, server_port)
    async with server:
        await server.serve_forever()

##############################################################################
#                                Main Program                                #
##############################################################################
if __name__ == "__main__":
    # Define server address and port
    server_addr = 'localhost'
    server_port = 5555

    # Run TCP server
    print("=====================================================")
    print("=                Running PYNQ Server                =")
    print("=====================================================")
    asyncio.run(run_server(server_addr=server_addr, server_port=server_port))


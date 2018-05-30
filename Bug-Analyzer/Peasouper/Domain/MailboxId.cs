﻿namespace Peasouper.Domain
{
   public struct MailboxId
    {
        readonly int _value;

        private MailboxId(int val)
        {
             _value = val;
        }

        public static explicit operator MailboxId(int value)
        {
            return new MailboxId(value);
        }

        public static implicit operator int(MailboxId me)
        {
            return me._value;
        }

        public static MailboxId? FromInt(int val)
        {
            return (val == 0) ? (MailboxId?)null : (MailboxId)val;
        }

        public override string ToString()
        {
            return _value.ToString();
        }
    }}
